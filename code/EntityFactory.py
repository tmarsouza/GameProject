import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'Level1Bg':
                return Background('Level1Bg', (0, 0))
            case 'Level2Bg':
                return Background('Level2Bg', (0, 0))
            case 'Player':
                return Player('Player', ((WIN_WIDTH / 2 - 15), WIN_HEIGHT - 125))
            case 'Enemy':
                choice = random.randint(0, 16)
                return Enemy(f'Ball_{choice}', (random.randint(0, WIN_WIDTH - 57), -60))

        return None
