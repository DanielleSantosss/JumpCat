import pygame

COLOR_BUE = (29, 32, 76)
COLOR_WHITE = (255, 255, 255)
COLOR_GREEN = (0, 128, 0)
COLOR_CYAN = (0, 128, 128)
COLOR_RED = (255, 0, 0)
COLOR_YELLOW = (255, 255, 0)

MENU_OPTION = (
    'NOVO JOGO',
    'SAIR'
)
GAMEOVER_OPTION = (
    'REINICIAR',
    'SAIR'
)

VICTORY_OPTION = (
    'JOGAR NOVAMENTE',
    'SAIR'
)

ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level2Bg0': 0,
    'Level2Bg1': 1,
    'Level2Bg2': 2,
    'Level2Bg3': 3,
    'Level3Bg0': 0,
    'Level3Bg1': 1,
    'Level3Bg2': 2,
    'Level4Bg0': 0,
    'Level4Bg1': 1,
    'Level4Bg2': 2,
    'Level4Bg3': 3,
    'Player1': 3,
    'Enemy1': 3,
    'Enemy2': 2
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level3Bg0': 999,
    'Level3Bg1': 999,
    'Level3Bg2': 999,
    'Level4Bg0': 999,
    'Level4Bg1': 999,
    'Level4Bg2': 999,
    'Level4Bg3': 999,
    'Player1': 300,
    'Enemy1': 999,
    'Enemy2': 999
}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level3Bg0': 0,
    'Level3Bg1': 0,
    'Level3Bg2': 0,
    'Level4Bg0': 0,
    'Level4Bg1': 0,
    'Level4Bg2': 0,
    'Level4Bg3': 0,
    'Player1': 0,
    'Enemy1': 100,
    'Enemy2': 150
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level3Bg0': 0,
    'Level3Bg1': 0,
    'Level3Bg2': 0,
    'Level4Bg0': 0,
    'Level4Bg1': 0,
    'Level4Bg2': 0,
    'Level4Bg3': 0,
    'Player1': 0,
    'Enemy1': 2,
    'Enemy2': 4
}

EVENT_TIMEOUT = pygame.USEREVENT + 2

EVENT_ENEMY = pygame.USEREVENT + 1

SPAWN_TIME = 3000

TIMEOUT_STEP = 100

WINDOW_WIDTH = 576
WINDOW_HEIGHT = 324
