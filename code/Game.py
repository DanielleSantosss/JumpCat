import pygame
from code.Const import MENU_OPTION, VICTORY_OPTION
from code.GameOver import GameOver
from code.Level import Level
from code.Menu import Menu
from code.Victory import Victory


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
                current_level = 'Level1'

                while self.running:
                    level = Level(self.window, current_level, menu_return, player_score)
                    level_return = level.run(player_score)

                    if not level_return:
                        game_over = GameOver(self.window)
                        choice = game_over.run()

                        if choice == "REINICIAR":
                            current_level = 'Level1'
                            continue
                        elif choice == "SAIR":
                            self.running = False
                            break

                    if current_level == 'Level1' and level_return:
                        current_level = 'Level2'
                    elif current_level == 'Level2' and level_return:
                        current_level = 'Level3'
                    elif current_level == 'Level3' and level_return:
                        current_level = 'Level4'
                    elif current_level == 'Level4' and level_return:
                        victory = Victory(self.window)
                        choice = victory.run()

                        if choice == VICTORY_OPTION[0]:
                            current_level = 'Level1'
                            continue
                        elif choice == VICTORY_OPTION[1]:
                            self.running = False
                            break

            elif menu_return == MENU_OPTION[1]:
                self.running = False

        pygame.quit()
        quit()
