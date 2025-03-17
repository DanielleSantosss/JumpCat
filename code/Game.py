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
                player_score = [0]
                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return = level.run(player_score)
                if level_return:
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    level.run(player_score)
                if level_return:
                    level = Level(self.window, 'Level3', menu_return, player_score)
                    level.run(player_score)
                if level_return:
                    level = Level(self.window, 'Level4', menu_return, player_score)
                    level.run(player_score)

            elif menu_return == MENU_OPTION[1]:
                self.running = False

        pygame.quit()
        quit()
