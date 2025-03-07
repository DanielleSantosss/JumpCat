import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_WHITE, EVENT_ENEMY, SPAWN_TIME
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Player import Player

class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.extend(EntityFactory.get_entity('Player1'))
        self.timeout = 20000
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)

    def run(self):
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

            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(14, f'FPS: {clock.get_fps() :.0f}', COLOR_WHITE, (10, 16))
            self.level_text(14, f'Entidades: {len(self.entity_list)}', COLOR_WHITE, (10, 25))

            pygame.display.flip()

        pygame.quit()
        sys.exit()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Sans-Titre Pro", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)