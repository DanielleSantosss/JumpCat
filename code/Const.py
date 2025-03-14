import pygame

COLOR_BUE = (29, 32, 76)
COLOR_WHITE = (255, 255, 255)
COLOR_GREEN = (0, 128, 0)
COLOR_CYAN = (0, 128, 128)

MENU_OPTION = (
    'NOVO JOGO',
    'PONTUAÇÃO',
    'SAIR'
)

ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Player1': 3,
    'Enemy1': 3,
    'Enemy2': 2
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Player1': 300,
    'Enemy1': 999,
    'Enemy2': 999
}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Player1': 0,
    'Enemy1': 100,
    'Enemy2': 200
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Player1': 0,
    'Enemy1': 2,
    'Enemy2': 4
}

EVENT_ENEMY = pygame.USEREVENT + 1

SPAWN_TIME = 4000

WINDOW_WIDTH = 576
WINDOW_HEIGHT = 324