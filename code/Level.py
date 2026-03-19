import sys

import pygame
from pygame.font import Font

from code.Const import WIN_HEIGHT, C_WHITE, EVENT_ENEMY, SPAWN_TIME, EVENT_TIMEOUT, TIMEOUT_TICK, \
    TIMEOUT_LEVEL, C_BLACK
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from pygame import Surface, Rect

from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:

    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.append(EntityFactory.get_entity(self.name + 'Bg'))
        player = EntityFactory.get_entity('Player')
        player.score = player_score[0]
        self.entity_list.append(player)
        self.timeout = TIMEOUT_LEVEL
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_TICK)

    def run(self, player_score: list[int]):
        pygame.mixer.music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.set_volume(0.05)
        pygame.mixer_music.play(-1)

        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, Player):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if ent.name == 'Player':
                    self.level_text(20, f'Player - Health: {ent.health} | Score: {ent.score}', C_BLACK, (155, 10))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    self.entity_list.append(EntityFactory.get_entity('Enemy'))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_TICK
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player':
                                player_score[0] = ent.score
                        return True

                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True

                if not found_player:
                    return False

            self.level_text(20, f'{self.name} - Time: {self.timeout / 1000:.1f}s', C_WHITE, (430, 10))
            self.level_text(20, f'Fps: {clock.get_fps():.0f}', C_WHITE, (35, WIN_HEIGHT - 35))
            self.level_text(20, f'Entidades: {len(self.entity_list)}', C_WHITE, (60, WIN_HEIGHT - 15))

            pygame.display.flip()
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Comic Sans MS", size=text_size)
        # text_font.set_bold(True)
        text_font.set_italic(True)
        text_surface: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rectangle: Rect = text_surface.get_rect(center=text_center_pos)
        self.window.blit(source=text_surface, dest=text_rectangle)
