import pygame
import random
from Laser import Laser

class enemies:
    rows, cols = (10, 10)
    # method 2 1st approach
    enemigos = [[0] * cols] * rows
    countenemies = None
    enemySkin1 = pygame.image.load("enemy1.png")
    enemySkin2 = pygame.image.load("enemy2.png")
    enemySkin3 = pygame.image.load("enemy3.png")
    enemyskinList=[enemySkin1,enemySkin2,enemySkin3]
    xmovement = None
    ymovement=None
    movementFlag =None
    clock = None
    animationIndex=0
    lasers = None
    def __init__(self):
        for i in range(0, 9):
            for j in range(0, 9):
                self.enemigos[i][j] = 1
        self.countenemies = 20
        self.xmovement = -3
        self.ymovement=-195
        self.clock=pygame.time.set_timer(pygame.USEREVENT, 1000,0)
        self.movementFlag =True #if is true, enemies move to right, else , move to left
        self.lasers = pygame.sprite.Group() #shooting of enemies

    def deleteEnemy(self, posx, posy):
        self.enemigos[posx][posy] = 0

    def isDead(self, posx, posy):
        if self.enemigos[posx][posy] != 0:
            return False
        else:
            return True

    def move(self): #debe de moverse de izquierda a derecha y siempre hacia abajo.
        if self.movementFlag ==True:
            if self.xmovement==5: #aritmetica para el movimiento :prueba y error
                self.ymovement+=10
                self.movementFlag =False
            else:
                self.xmovement+=1
        else:
            if self.xmovement==-2:
                self.ymovement+=10
                self.movementFlag =True
            else:
                self.xmovement-=1
    def shooting(self):
        #note to self, bc how the lasers were programed, will only shoot if the spawn
        #is greater than -10 , so , if the player doesnt kill the aliens, this probability
        #will increase, making the game harder, (its not a bug its a freature!)
        n = random.randint(0,9)
        h = random.randint(0,9)
        self.lasers.add(Laser((40 + 40 * n + 30 * self.xmovement, 25 * h + self.ymovement),+3 , "red"))
    def updateLasers(self):
        self.lasers.update()



