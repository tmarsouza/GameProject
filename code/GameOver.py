import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_WHITE, WIN_WIDTH, MENU_OPTION_GAME_OVER, C_CYAN


class GameOver:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/GameOverBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./asset/GameOver.mp3')
        pygame.mixer_music.set_volume(0.05)
        pygame.mixer_music.play(-1)
        while True:

            self.window.blit(source=self.surf, dest=self.rect)
            self.game_over_text(90, "GAME OVER", C_WHITE, ((WIN_WIDTH / 2), 120))
            self.game_over_text(90, "TRY AGAIN", C_WHITE, ((WIN_WIDTH / 2), 240))

            for i in range(len(MENU_OPTION_GAME_OVER)):
                if i == menu_option:
                    self.game_over_text(65, MENU_OPTION_GAME_OVER[i], C_CYAN, ((WIN_WIDTH / 2), 600 + 90 * i))
                else:
                    self.game_over_text(65, MENU_OPTION_GAME_OVER[i], C_WHITE, ((WIN_WIDTH / 2), 600 + 90 * i))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('Exiting.')
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # DOWN KEY
                        if menu_option < len(MENU_OPTION_GAME_OVER) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION_GAME_OVER) - 1
                    if event.key == pygame.K_RETURN:  # ENTER
                        return MENU_OPTION_GAME_OVER[menu_option]

    def game_over_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Comic Sans MS", size=text_size)
        text_surface: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rectangle: Rect = text_surface.get_rect(center=text_center_pos)
        self.window.blit(source=text_surface, dest=text_rectangle)
