import pygame
import random
from Laser import Laser

class enemy(pygame.sprite.Sprite):
    countenemies = None
    enemySkin1 = pygame.image.load("enemy1.png")
    enemySkin2 = pygame.image.load("enemy2.png")
    enemySkin3 = pygame.image.load("enemy3.png")
    enemyskinList=[enemySkin1,enemySkin2,enemySkin3]
    contadorx=None
    movementFlag =None
    animationIndex=0
    lasers = None
    def __init__(self, xpos, ypos):
        super().__init__()
        self.countenemies = 20

        self.clock=pygame.time.set_timer(pygame.USEREVENT, 1000,0)
        self.movementFlag =True #if is true, enemies move to right, else , move to left
        self.lasers = pygame.sprite.Group() #shooting of enemies
        self.image=self.enemySkin1 #this has to be done this way bc of inheritance
        self.rect = self.image.get_rect(center=(xpos,ypos))
        self.contadorx= 0


#this method needs to be called update because of polimorfism
    def update(self): #debe de moverse de izquierda a derecha y siempre hacia abajo.
        if self.movementFlag ==True:
            if self.contadorx==7: #aritmetica para el movimiento :prueba y error
                self.rect.y+=20
                self.movementFlag =False
            else:
                self.rect.x+=20
                self.contadorx+=1
        else:
            if self.contadorx==0:
                self.rect.y+=20
                self.movementFlag =True
            else:
                self.rect.x-=20
                self.contadorx -= 1
                #print("el contador es:"+str(self.contadorx))
    def shooting(self):
        #note to self, bc how the lasers were programed, will only shoot if the spawn
        #is greater than -10 , so , if the player doesnt kill the aliens, this probability
        #will increase, making the game harder, (its not a bug its a freature!)
        n = random.randint(0,9)
        h = random.randint(0,9)
        self.lasers.add(Laser((40 + 40 * n + 30 * self.rect.x, 25 * h + self.rect.y),+3 , "red"))
    def updateLasers(self):
        self.lasers.update()



