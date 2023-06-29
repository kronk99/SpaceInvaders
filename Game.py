#gameclass, will work ass the class that will contain everything
import pygame
from sys import exit
class Game:
    # private: this is put bc c++ or java sintax #
    runflag = False
    startFlag = False
    gameFlag =False
    nivel = None #type int
    startScreen = None
    lvl1Screen = None
    clock = pygame.time.Clock()

    def __init__(self): #constructor de la clase
        pygame.init()
        self.nivel=1
        self.startScreen=pygame.display.set_mode((800,400))
        self.runflag =True
        pygame.display.set_caption("SpaceInvaders")


    def lvlUp(self):
        self.nivel+=1
    def run(self):
        while self.runflag ==True:
            self.eventHandler()
            pygame.display.update()  # actualiza el display ,deberia de ir en el metodo update.
            self.clock.tick(60) # maximum frame rate
    def eventHandler(self): #manejador de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.runflag=False
                exit()