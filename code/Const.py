# C
import pygame

COLOR_PURPLE = (160, 32, 240)
COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_WHITE = (255, 255, 255)

# E
ENTITY_SPEED = {
    'Player': 5,
    'Enemy': 2

}
EVENT_ENEMY = pygame.USEREVENT + 1

# M
MENU_OPTION = ('NEW GAME',
               'SCORE',
               'EXIT'
               )

# P
PLAYER_KEY_LEFT = {'Player': pygame.K_LEFT}
PLAYER_KEY_RIGHT = {'Player': pygame.K_RIGHT}
PLAYER_KEY_SHOOT = {'Player': pygame.K_SPACE}

# W
WIN_WIDTH = 536
WIN_HEIGHT = 953
