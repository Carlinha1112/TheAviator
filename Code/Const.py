# C
import pygame

C_BLUE = (22, 65, 124)
C_YELLOW = (255, 253, 85)
C_WHITE = (255, 255, 255)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_COIN = pygame.USEREVENT + 1

ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Player': 3,
    'Enemy1Lv1': 12,
    'Enemy2Lv1': 14,
    'Enemy3Lv1': 14,
    'Coin': 13,
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Player': 50,
    'Enemy1Lv1': 999,
    'Enemy2Lv1': 999,
    'Enemy3Lv1': 999,
    'Coin': 999,
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Player': 0,
    'Enemy1Lv1': 0,
    'Enemy2Lv1': 0,
    'Enemy3Lv1': 0,
    'Coin': 10,
}

# M
MENU_OPTION = ('NEW GAME', 'SCORE', 'EXIT')

# S
SPAWN_TIME = 4000

# W
WIN_WIDTH = 941
WIN_HEIGHT = 529