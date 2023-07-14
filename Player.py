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
    player_gravity =None
    isJumping =None
    def __init__(self):
        super().__init__()
        self.rect = self.playerSkin1.get_rect(center = (300,370))
        self.laser_time=0
        self.laser_cooldown=600
        self.lasers =pygame.sprite.Group()
        self.player_gravity = 0
    def checkLimits(self , movementx ):
        if self.rect.x + movementx > 0 and self.rect.x+ movementx <550:
            self.rect.x += movementx
    #for the gravity and jumping purposes
    def gravity(self):
        if self.rect.y <360 :
            self.player_gravity+=1
            if self.rect.y+self.player_gravity >=360:
                self.rect.y =360
                self.player_gravity =0
        self.rect.y += self.player_gravity
    def jump(self):
        print("saltando")
        if self.rect.y>=360:
            self.player_gravity=-15
    #end of gravity
    def getrect(self ,number):
        self.playerRect =self.playerList[int(number)]
        return self.playerRect
    def shoot(self ):
        self.lasers.add(Laser((self.rect.x+20 ,self.rect.y)  ,-3,"green"))
    def updateLaser(self):
        self.lasers.update()
