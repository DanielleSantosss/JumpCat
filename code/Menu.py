import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WINDOW_WIDTH, COLOR_BUE, MENU_OPTION, COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/Menu.png').convert_alpha()
        self.rect = self.surf.get_rect()
        self.running = True

        self.cat_surf = pygame.image.load('./assets/Player1.png').convert_alpha()
        self.cat_rect = self.cat_surf.get_rect()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Sans-Titre Pro", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    def run(self):
        menu_option = 0
        pygame.mixer.music.load('./assets/Menu.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        while self.running:
            self.window.blit(self.surf, self.rect)
            self.menu_text(70, "Jump Cat", COLOR_BUE, ((WINDOW_WIDTH / 2), 90))
            self.cat_rect.center = (WINDOW_WIDTH / 2, 140)
            self.window.blit(self.cat_surf, self.cat_rect)

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(35, MENU_OPTION[i], COLOR_BUE, ((WINDOW_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(35, MENU_OPTION[i], COLOR_WHITE, ((WINDOW_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.mixer.music.stop()
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

                if event.type == pygame.MOUSEMOTION:
                    mouse_pos = pygame.mouse.get_pos()
                    for i in range(len(MENU_OPTION)):
                        text_rect = pygame.Rect(
                            (WINDOW_WIDTH / 2 - 100, 200 + 25 * i - 15),
                            (200, 30)
                        )
                        if text_rect.collidepoint(mouse_pos):
                            menu_option = i

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for i in range(len(MENU_OPTION)):
                        text_rect = pygame.Rect(
                            (WINDOW_WIDTH / 2 - 100, 200 + 25 * i - 15),
                            (200, 30)
                        )
                        if text_rect.collidepoint(mouse_pos):
                            menu_option = i
                            return MENU_OPTION[menu_option]

        return True
