import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WINDOW_WIDTH, COLOR_WHITE, COLOR_GREEN, COLOR_YELLOW, VICTORY_OPTION


class Victory:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/Victory.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, self.window.get_size())
        self.rect = self.surf.get_rect(topleft=(0, 0))
        self.running = True
        self.menu_option = 0

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font(None, text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    def run(self):
        pygame.mixer.music.load('./assets/Victory.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(0)

        while self.running:
            self.window.blit(self.surf, self.rect)

            self.menu_text(50, "PARABÉNS, VOCÊ VENCEU!", COLOR_GREEN, (WINDOW_WIDTH / 2, 90))

            for i, option in enumerate(VICTORY_OPTION):
                color = COLOR_YELLOW if i == self.menu_option else COLOR_WHITE
                self.menu_text(40, option, color, (WINDOW_WIDTH / 2, 200 + 50 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return 'SAIR'

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.menu_option = (self.menu_option + 1) % len(VICTORY_OPTION)
                    if event.key == pygame.K_UP:
                        self.menu_option = (self.menu_option - 1) % len(VICTORY_OPTION)
                    if event.key == pygame.K_RETURN:
                        return VICTORY_OPTION[self.menu_option]

                if event.type == pygame.MOUSEMOTION:
                    mouse_pos = pygame.mouse.get_pos()
                    for i in range(len(VICTORY_OPTION)):
                        text_rect = pygame.Rect(
                            (WINDOW_WIDTH / 2 - 100, 200 + 50 * i - 20),
                            (200, 40)
                        )
                        if text_rect.collidepoint(mouse_pos):
                            self.menu_option = i

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for i in range(len(VICTORY_OPTION)):
                        text_rect = pygame.Rect(
                            (WINDOW_WIDTH / 2 - 100, 200 + 50 * i - 20),
                            (200, 40)
                        )
                        if text_rect.collidepoint(mouse_pos):
                            return VICTORY_OPTION[i]
