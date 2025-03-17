import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_WHITE, EVENT_ENEMY, SPAWN_TIME, COLOR_GREEN, EVENT_TIMEOUT, TIMEOUT_STEP, GAMEOVER_OPTION
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.GameOver import GameOver
from code.Player import Player


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        player = EntityFactory.get_entity('Player1')[0]
        player.score = player_score[0]
        self.entity_list.append(player)
        self.timeout = 30000
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self, player_score: list[int]):
        pygame.mixer_music.load(f'./assets/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        running = True

        while running:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    new_enemies = EntityFactory.get_entity(choice)
                    self.entity_list.extend(new_enemies)
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for entity in self.entity_list:
                            if isinstance(entity, Player) and entity.name == 'Player1':
                                player_score[0] = entity.score
                        return True

                found_player = False
                for entity in self.entity_list:
                    if isinstance(entity, Player):
                        found_player = True

                if not found_player:
                    return False

            keys = pygame.key.get_pressed()
            for entity in self.entity_list:
                if isinstance(entity, Player):
                    if keys[pygame.K_a]:
                        entity.move_left()
                    elif keys[pygame.K_d]:
                        entity.move_right()
                    else:
                        entity.stop()
                    if keys[pygame.K_SPACE]:
                        entity.jump()

            self.window.fill((0, 0, 0))

            for entity in self.entity_list:
                if isinstance(entity, Entity):
                    self.window.blit(entity.surface, entity.rect)
                    entity.move()
                    if entity.name == 'Player1':
                        self.level_text(15, f'Player - Vida: {entity.health} | Pontuação: {entity.score}', COLOR_GREEN,
                                        (10, 36))

            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(14, f'FPS: {clock.get_fps() :.0f}', COLOR_WHITE, (10, 16))
            self.level_text(14, f'Entidades: {len(self.entity_list)}', COLOR_WHITE, (10, 26))

            pygame.display.flip()

            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

            for entity in self.entity_list:
                if isinstance(entity, Player) and entity.health <= 0:
                    pygame.mixer_music.stop()
                    game_over = GameOver(self.window)
                    choice = game_over.run()

                    if choice == GAMEOVER_OPTION[0]:
                        return True
                    elif choice == GAMEOVER_OPTION[1]:
                        return False

        pygame.quit()
        sys.exit()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Sans-Titre Pro", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
