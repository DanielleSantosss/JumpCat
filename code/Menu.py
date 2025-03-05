import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WINDOW_WIDTH, COLOR_BUE, MENU_OPTION, COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/Menu.png')
        self.rect = self.surf.get_rect()
        self.running = True

        self.cat_surf = pygame.image.load('./assets/Cat.png').convert_alpha()
        self.cat_rect = self.cat_surf.get_rect()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Sans-Titre Pro", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    def run(self):
        pygame.mixer.music.load('./assets/Menu.mp3')
        pygame.mixer.music.play(-1)

        while self.running:
            self.window.blit(self.surf, self.rect)
            self.menu_text(70, "Jump Cat", COLOR_BUE, ((WINDOW_WIDTH / 2), 70))
            self.cat_rect.center = (WINDOW_WIDTH / 2, 140)
            self.window.blit(self.cat_surf, self.cat_rect)

            for i in range(len(MENU_OPTION)):
                self.menu_text(30, MENU_OPTION[i], COLOR_WHITE, ((WINDOW_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return False

        return True
