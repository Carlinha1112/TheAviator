# C
import pygame

C_BLUE = (22, 65, 124)
C_YELLOW = (255, 253, 85)
C_WHITE = (255, 255, 255)
C_RED = (247, 29, 38)
C_PINK = (247, 26, 165)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_COIN = pygame.USEREVENT + 2
EVENT_TIMEOUT = pygame.USEREVENT + 3

ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level2Bg0': 0,
    'Level2Bg1': 1,
    'Level2Bg2': 2,
    'Level2Bg3': 3,
    'Level2Bg4': 4,
    'Level2Bg5': 5,
    'Player': 4,
    'Enemy1Lv1': 12,
    'Enemy2Lv1': 14,
    'Enemy3Lv1': 14,
    'Enemy1Lv2': 14,
    'Enemy2Lv2': 14,
    'Enemy3Lv2': 15,
    'Enemy4Lv2': 15,
    'Coin': 10,
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,
    'Level2Bg5': 999,
    'Player': 50,
    'Enemy1Lv1': 999,
    'Enemy2Lv1': 999,
    'Enemy3Lv1': 999,
    'Enemy1Lv2': 999,
    'Enemy2Lv2': 999,
    'Enemy3Lv2': 999,
    'Enemy4Lv2': 999,
    'Coin': 999,
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Level2Bg5': 0,
    'Player': 0,
    'Enemy1Lv1': 0,
    'Enemy2Lv1': 0,
    'Enemy3Lv1': 0,
    'Enemy1Lv2': 0,
    'Enemy2Lv2': 0,
    'Enemy3Lv2': 0,
    'Enemy4Lv2': 0,
    'Coin': 10,
}

# M
MENU_OPTION = ('NEW GAME', 'SCORE', 'EXIT')

# S
SPAWN_TIME = 5000
SPAWN_TIME_LEVEL1 = 3000
SPAWN_TIME_LEVEL2 = 1500

# T
TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 20000

# W
WIN_WIDTH = 941
WIN_HEIGHT = 529

# S
SCORE_POS = {'Title': (WIN_WIDTH / 2, 100),
             'EnterName': (WIN_WIDTH / 2, 180),
             'Label': (WIN_WIDTH / 2, 200),
             'Name': (WIN_WIDTH / 2, 220),
             0: (WIN_WIDTH / 2, 280),
             1: (WIN_WIDTH / 2, 300),
             2: (WIN_WIDTH / 2, 320),
             3: (WIN_WIDTH / 2, 340),
             4: (WIN_WIDTH / 2, 360),
             5: (WIN_WIDTH / 2, 380),
             6: (WIN_WIDTH / 2, 400),
             7: (WIN_WIDTH / 2, 420),
             8: (WIN_WIDTH / 2, 440),
             9: (WIN_WIDTH / 2, 460),
             }
