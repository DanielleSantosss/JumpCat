import pygame
from code.Const import MENU_OPTION
from code.Level import Level
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((576, 324))
        self.running = True

    def run(self):
        menu = Menu(self.window)

        while self.running:
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0]]:
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()

            elif menu_return == MENU_OPTION[2]:
                self.running = False

        pygame.quit()
        quit()
