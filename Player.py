import pygame
from Laser import Laser
class player(pygame.sprite.Sprite):
    playerSkin1 = pygame.image.load("player1.png")
    playerSkin2 = pygame.image.load("player2.png")
    playerSkin3 = pygame.image.load("player3.png")
    playerList = [playerSkin1, playerSkin2, playerSkin3]
    playerRect = None
    xmovement = None
    ymovement = None
    laser_time=None
    laser_cooldown=None
    lasers=None
    def __init__(self):
        super().__init__()
        self.xmovement = 300
        self.ymovement = 350
        self.playerRect = self.playerSkin1.get_rect(center = (self.xmovement,self.ymovement))
        self.laser_time=0
        self.laser_cooldown=600
        self.lasers =pygame.sprite.Group()
    def checkLimits(self , movementx ):
        if self.xmovement + movementx > 0 and self.xmovement + movementx <550:
            self.xmovement += movementx
    def getrect(self ,number):
        self.playerRect =self.playerList[int(number)]
        return self.playerRect
    def shoot(self ):
        self.lasers.add(Laser((self.xmovement+20 ,self.ymovement)  ,-3,"green"))
    def updateLaser(self):
        self.lasers.update()
