import sys
import random

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_HEIGHT, COLOR_WHITE, EVENT_ENEMY
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from pygame import Surface, Rect


class Level:

    def __init__(self, window: Surface, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.append(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player'))
        self.timeout = 20000
        pygame.time.set_timer(EVENT_ENEMY, 2000)




    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                if ent.name == 'Player':
                    ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    self.entity_list.append(EntityFactory.get_entity('Enemy'))
                    print(self.entity_list)


            self.level_text(20, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', COLOR_WHITE, (35, 10))
            self.level_text(20, f'Fps: {clock.get_fps():.0f}', COLOR_WHITE, (35, WIN_HEIGHT - 35))
            self.level_text(20, f'Entidades: {len(self.entity_list)}', COLOR_WHITE, (60, WIN_HEIGHT - 20))
            pygame.display.flip()


    def   level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name = "Comic Sans MS", size = text_size)
        text_surface: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rectangle: Rect = text_surface.get_rect(center = text_center_pos)
        self.window.blit(source=text_surface, dest=text_rectangle)