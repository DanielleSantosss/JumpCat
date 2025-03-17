from code import Player
from code.Background import Background
from code.Const import WINDOW_WIDTH
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(4):
                    list_bg.append(Background(f'Level1Bg{i}', position))
                    list_bg.append(Background(f'Level1Bg{i}', (WINDOW_WIDTH, 0)))
                return list_bg
            case 'Level2Bg':
                list_bg = []
                for i in range(4):
                    list_bg.append(Background(f'Level2Bg{i}', position))
                    list_bg.append(Background(f'Level2Bg{i}', (WINDOW_WIDTH, 0)))
                return list_bg
            case 'Level3Bg':
                list_bg = []
                for i in range(3):
                    list_bg.append(Background(f'Level3Bg{i}', position))
                    list_bg.append(Background(f'Level3Bg{i}', (WINDOW_WIDTH, 0)))
                return list_bg
            case 'Level4Bg':
                list_bg = []
                for i in range(4):
                    list_bg.append(Background(f'Level4Bg{i}', position))
                    list_bg.append(Background(f'Level4Bg{i}', (WINDOW_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return [Player('Player1', (10, 250))]
            case 'Enemy1':
                return [Enemy('Enemy1', (WINDOW_WIDTH + 50, 255))]
            case 'Enemy2':
                return [Enemy('Enemy2', (WINDOW_WIDTH + 50, 255))]
