import pygame
from Laser import Laser
class player(pygame.sprite.Sprite):
    rect = None
    playerSkin1 = pygame.image.load("player1.png")
    playerSkin2 = pygame.image.load("player2.png")
    playerSkin3 = pygame.image.load("player3.png")
    playerList = [playerSkin1, playerSkin2, playerSkin3]
    laser_time=None
    laser_cooldown=None
    lasers=None
    def __init__(self):
        super().__init__()
        self.rect = self.playerSkin1.get_rect(center = (300,370))
        self.laser_time=0
        self.laser_cooldown=600
        self.lasers =pygame.sprite.Group()
    def checkLimits(self , movementx ):
        if self.rect.x + movementx > 0 and self.rect.x+ movementx <550:
            self.rect.x += movementx
    def getrect(self ,number):
        self.playerRect =self.playerList[int(number)]
        return self.playerRect
    def shoot(self ):
        self.lasers.add(Laser((self.rect.x+20 ,self.rect.y)  ,-3,"green"))
    def updateLaser(self):
        self.lasers.update()
