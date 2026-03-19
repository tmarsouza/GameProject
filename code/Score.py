import sys
from datetime import datetime

import pygame
from pygame import Surface, Rect, K_RETURN, KEYDOWN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font

from code.Const import C_WHITE, SCORE_POS, MENU_OPTION
from code.DBProxy import DBProxy


class Score:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def save_score(self, game_mode: str, player_score: list[int]):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.set_volume(0.05)
        pygame.mixer_music.play(-1)
        db_proxy = DBProxy('DBScore')
        name = ''
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(30, 'CONGRATULATIONS!!!', C_WHITE, SCORE_POS['Title'])
            score = player_score[0]
            text = 'Enter your name (4 characters):'
            if game_mode == MENU_OPTION[0]:
                score = player_score[0]
            self.score_text(30, text, C_WHITE, SCORE_POS['EnterName'])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4:
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                        self.show_score()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode
            self.score_text(30, name, C_WHITE, SCORE_POS['Name'])
            pygame.display.flip()
            pass

    def show_score(self):
        # pygame.mixer_music.load('./asset/Score.mp3')    LOAD THE MUSIC
        # pygame.mixer_music.play(-1)     PLAY THE MUSIC
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(50, 'TOP 10 SCORE', C_WHITE, SCORE_POS['Title'])
        self.score_text(20, 'NAME      SCORE        DATE        ', C_WHITE, SCORE_POS['Label'])
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.fetch_top10()
        db_proxy.close()

        for player_score in list_score:
            id_, name, score, date = player_score
            self.score_text(20, f'{name}         {score :05d}        {date}', C_WHITE,
                            SCORE_POS[list_score.index(player_score)])

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Comic Sans MS", size=text_size)
        text_surface: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rectangle: Rect = text_surface.get_rect(center=text_center_pos)
        self.window.blit(source=text_surface, dest=text_rectangle)


def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"
