import pygame

# C
C_PURPLE = (160, 32, 240)
C_BLACK = (0, 0, 0)
C_BLUE = (0, 0, 255)
C_WHITE = (255, 255, 255)
C_CYAN = (0, 128, 128)
C_PINK = (255, 51, 153)

# E
ENTITY_SPEED = {
    'Player': 5.5,
    'Ball_0': 1.5,
    'Ball_1': 1.5,
    'Ball_2': 1.5,
    'Ball_3': 1.5,
    'Ball_4': 1.5,
    'Ball_5': 1.5,
    'Ball_6': 1.5,
    'Ball_7': 1.5,
    'Ball_8': 1.5,
    'Ball_9': 1.5,
    'Ball_10': 1.5,
    'Ball_11': 1.5,
    'Ball_12': 1.5,
    'Ball_13': 1.5,
    'Ball_14': 1.5,
    'Ball_15': 1.5,
    'Ball_16': 1.5,
    'PlayerShot': 3.5
}

ENTITY_HEALTH = {
    'Level1Bg': 999,
    'Level2Bg': 999,
    'Player': 3,
    'PlayerShot': 1,
    'Ball_0': 100,
    'Ball_1': 100,
    'Ball_2': 100,
    'Ball_3': 100,
    'Ball_4': 100,
    'Ball_5': 100,
    'Ball_6': 100,
    'Ball_7': 100,
    'Ball_8': 100,
    'Ball_9': 100,
    'Ball_10': 100,
    'Ball_11': 100,
    'Ball_12': 100,
    'Ball_13': 100,
    'Ball_14': 100,
    'Ball_15': 100,
    'Ball_16': 100
}

ENTITY_DAMAGE = {
    'Level1Bg': 0,
    'Level2Bg': 0,
    'Player': 0,
    'PlayerShot': 100,
    'Ball_0': 100,
    'Ball_1': 100,
    'Ball_2': 100,
    'Ball_3': 100,
    'Ball_4': 100,
    'Ball_5': 100,
    'Ball_6': 100,
    'Ball_7': 100,
    'Ball_8': 100,
    'Ball_9': 100,
    'Ball_10': 100,
    'Ball_11': 100,
    'Ball_12': 100,
    'Ball_13': 100,
    'Ball_14': 100,
    'Ball_15': 100,
    'Ball_16': 100
}

ENTITY_SCORE = {
    'Level1Bg': 0,
    'Level2Bg': 0,
    'Player': 0,
    'PlayerShot': 0,
    'Ball_0': 100,
    'Ball_1': 100,
    'Ball_2': 100,
    'Ball_3': 100,
    'Ball_4': 100,
    'Ball_5': 100,
    'Ball_6': 100,
    'Ball_7': 100,
    'Ball_8': 100,
    'Ball_9': 100,
    'Ball_10': 100,
    'Ball_11': 100,
    'Ball_12': 100,
    'Ball_13': 100,
    'Ball_14': 100,
    'Ball_15': 100,
    'Ball_16': 100
}

ENTITY_SHOT_DELAY = {
    'Player': 20

}

EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

# M
MENU_OPTION = ('NEW GAME',
               'SCORE',
               'EXIT'
               )

MENU_OPTION_GAME_OVER = 'BACK TO MENU',

# P
PLAYER_KEY_LEFT = {'Player': pygame.K_LEFT}
PLAYER_KEY_RIGHT = {'Player': pygame.K_RIGHT}
PLAYER_KEY_SHOOT = {'Player': pygame.K_SPACE}

# S
SPAWN_TIME = 1000

# T
TIMEOUT_TICK = 100  # 0.1 seconds
TIMEOUT_LEVEL = 20000  # 20 seconds

# W
WIN_WIDTH = 536
WIN_HEIGHT = 953

# S
SCORE_POS = {'Title': (WIN_WIDTH / 2, 70),
             'EnterName': (WIN_WIDTH / 2, 115),
             'Label': ((WIN_WIDTH / 2) - 10, 115),
             'Name': (WIN_WIDTH / 2, 165),
             0: (WIN_WIDTH / 2 + 20, 140),
             1: (WIN_WIDTH / 2 + 20, 160),
             2: (WIN_WIDTH / 2 + 20, 180),
             3: (WIN_WIDTH / 2 + 20, 200),
             4: (WIN_WIDTH / 2 + 20, 220),
             5: (WIN_WIDTH / 2 + 20, 240),
             6: (WIN_WIDTH / 2 + 20, 260),
             7: (WIN_WIDTH / 2 + 20, 280),
             8: (WIN_WIDTH / 2 + 20, 300),
             9: (WIN_WIDTH / 2 + 20, 320),
             }
