#gameclass, will work ass the class that will contain everything
import pygame
from Button import Button
from sys import exit
class Game:
    # private: this is put bc c++ or java sintax #
    runflag = False
    startFlag = False
    gameFlag =False
    Screen = 0
    nivel = None #type int
    startScreen = None
    lvl1Screen = None
    clock = pygame.time.Clock()

    def __init__(self): #constructor de la clase
        pygame.init()
        self.nivel=1
        self.startScreen=pygame.display.set_mode((800,400))
        self.Screen =1
        pygame.display.set_caption("SpaceInvaders")

    def get_font(self,size):  # Returns Press-Start-2P in the desired size
        return pygame.font.Font("Pixeltype.ttf", size)
    def lvlUp(self):
        self.nivel+=1
    def run(self):
        while self.Screen !=0:
            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = self.get_font(100).render("MAIN MENU", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))

            PLAY_BUTTON = Button(image=None, pos=(400, 150),
                                    text_input="PLAY", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
            OPTIONS_BUTTON = Button(image=None, pos=(400, 200),
                                        text_input="OPTIONS", font=self.get_font(75), base_color="#d7fcd4",
                                        hovering_color="White")
            QUIT_BUTTON = Button( image=None,pos=(400, 250),
                                     text_input="QUIT", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")

            self.startScreen.blit(MENU_TEXT, MENU_RECT)

            for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.startScreen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.Screen = 0
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                           self.play()
                    if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.options()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        self.Screen = 0
                        exit()
            pygame.display.update()  # actualiza el display ,deberia de ir en el metodo update.
            self.clock.tick(60) # maximum frame rate
    def play(self):
        print("hola")
    def options(self):
        print("xd")