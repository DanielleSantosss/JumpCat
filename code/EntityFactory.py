from code import Player
from code.Background import Background
from code.Const import WINDOW_WIDTH, WINDOW_HEIGHT
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
            case 'Player1':
                return [Player('Player1', (10, 240))]
            case 'Enemy1':
                return [Enemy('Enemy1', (WINDOW_WIDTH + 10, 250))]
            case 'Enemy2':
                return [Enemy('Enemy2', (WINDOW_WIDTH + 10, 255))]