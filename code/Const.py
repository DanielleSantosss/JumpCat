import pygame

COLOR_BUE = (29, 32, 76)
COLOR_WHITE = (255, 255, 255)

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
    'Enemy1': 3,
    'Enemy2': 2
}

EVENT_ENEMY = pygame.USEREVENT + 1

SPAWN_TIME = 4000

WINDOW_WIDTH = 576
WINDOW_HEIGHT = 324