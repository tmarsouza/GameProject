import pygame

from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_PURPLE, COLOR_BLACK, MENU_OPTION


class Menu:
    def __init__(self, window):
        self.window = window
        self.surface = pygame.image.load('./asset/Backgrounds/Bg_01.png')
        self.rectangle = self.surface.get_rect(left=0, top=0)

    def run(self, ):
        # pygame.mixer_music.load('./asset/Sounds/Menu.mp3')    LOAD THE MUSIC
        # pygame.mixer_music.play(-1)     PLAY THE MUSIC
        while True:
            self.window.blit(source=self.surface, dest=self.rectangle)
            self.menu_text(120, "Fever", COLOR_PURPLE, ((WIN_WIDTH / 2), 120))
            self.menu_text(120, "Dream", COLOR_PURPLE, ((WIN_WIDTH / 2), 240))


            for i in range(len(MENU_OPTION)):
                self.menu_text(75, MENU_OPTION[i], COLOR_BLACK, ((WIN_WIDTH / 2), 600 + 90 * i))



            pygame.display.flip()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('Exiting.')
                    pygame.quit()
                    quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name = "Comic Sans MS", size = text_size)
        text_surface: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rectangle: Rect = text_surface.get_rect(center = text_center_pos)
        self.window.blit(source=text_surface, dest=text_rectangle)

