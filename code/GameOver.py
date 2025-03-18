import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WINDOW_WIDTH, GAMEOVER_OPTION, COLOR_WHITE, COLOR_RED


class GameOver:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/GameOver.png').convert_alpha()

        self.surf = pygame.transform.scale(self.surf, self.window.get_size())

        self.rect = self.surf.get_rect(topleft=(0, 0))
        self.running = True

        self.cat_surf = pygame.image.load('./assets/PlayerDeath.png').convert_alpha()
        self.cat_rect = self.cat_surf.get_rect(center=(WINDOW_WIDTH / 2, 140))

        self.menu_death_option = 0
        self.fade_alpha = 0

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, bold=False):
        text_font: Font = pygame.font.SysFont("Sans-Titre Pro", text_size, bold=bold)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)

    def run(self):
        pygame.mixer.music.load('./assets/GameOver.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(0)

        clock = pygame.time.Clock()

        while self.running:
            self.window.fill((0, 0, 0))
            self.surf.set_alpha(self.fade_alpha)
            self.window.blit(self.surf, self.rect)

            self.menu_text(70, "GAME OVER", COLOR_RED, ((WINDOW_WIDTH / 2), 90), bold=True)
            self.window.blit(self.cat_surf, self.cat_rect)

            for i, option in enumerate(GAMEOVER_OPTION):
                color = COLOR_RED if i == self.menu_death_option else COLOR_WHITE
                self.menu_text(35, option, color, ((WINDOW_WIDTH / 2), 200 + 40 * i))

            pygame.display.flip()
            clock.tick(30)

            if self.fade_alpha < 255:
                self.fade_alpha += 10

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return False

                if event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_DOWN, pygame.K_s]:
                        self.menu_death_option = (self.menu_death_option + 1) % len(GAMEOVER_OPTION)
                    if event.key in [pygame.K_UP, pygame.K_w]:
                        self.menu_death_option = (self.menu_death_option - 1) % len(GAMEOVER_OPTION)
                    if event.key == pygame.K_RETURN:
                        return GAMEOVER_OPTION[self.menu_death_option]

                if event.type == pygame.MOUSEMOTION:
                    mouse_pos = pygame.mouse.get_pos()
                    for i, option in enumerate(GAMEOVER_OPTION):
                        text_rect = Rect((WINDOW_WIDTH / 2 - 100, 200 + 40 * i - 15), (200, 30))
                        if text_rect.collidepoint(mouse_pos):
                            self.menu_death_option = i

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for i, option in enumerate(GAMEOVER_OPTION):
                        text_rect = Rect((WINDOW_WIDTH / 2 - 100, 200 + 40 * i - 15), (200, 30))
                        if text_rect.collidepoint(mouse_pos):
                            return GAMEOVER_OPTION[i]

        return True
