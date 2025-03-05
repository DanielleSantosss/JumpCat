import pygame
from code.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((576, 324))
        self.running = True

    def run(self):
        menu = Menu(self.window)

        while self.running:
            if not menu.run():
                self.running = False

        pygame.quit()
        quit()