import pygame

from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, C_PURPLE, C_BLACK, MENU_OPTION, C_BLUE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)


    def run(self, ):
        menu_option = 0
        # pygame.mixer_music.load('./asset/Sounds/Menu.mp3')    LOAD THE MUSIC
        # pygame.mixer_music.play(-1)     PLAY THE MUSIC
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(120, "Fever", C_PURPLE, ((WIN_WIDTH / 2), 120))
            self.menu_text(120, "Dream", C_PURPLE, ((WIN_WIDTH / 2), 240))

            for i in range(len(MENU_OPTION)):

                if i == menu_option:
                    self.menu_text(75, MENU_OPTION[i], C_BLUE, ((WIN_WIDTH / 2), 600 + 90 * i))
                else:
                    self.menu_text(75, MENU_OPTION[i], C_BLACK, ((WIN_WIDTH / 2), 600 + 90 * i))
            pygame.display.flip()



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('Exiting.')
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  #DOWN KEY
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  #UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:  #ENTER
                        return MENU_OPTION[menu_option]



    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name = "Comic Sans MS", size = text_size)
        text_surface: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rectangle: Rect = text_surface.get_rect(center = text_center_pos)
        self.window.blit(source=text_surface, dest=text_rectangle)

