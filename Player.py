import pygame
class player:
    playerSkin1 = pygame.image.load("player1.png")
    playerSkin2 = pygame.image.load("player2.png")
    playerSkin3 = pygame.image.load("player3.png")
    playerList = [playerSkin1, playerSkin2, playerSkin3]
    playerRect = None
    xmovement = None
    ymovement = None
    def __init__(self):
        self.xmovement = 300
        self.ymovement = 350
        self.playerRect = self.playerSkin1.get_rect(center = (self.xmovement,self.ymovement))
    def checkLimits(self , movementx ):
        if self.xmovement + movementx > 0 and self.xmovement + movementx <550:
            self.xmovement += movementx
    def getrect(self ,number):
        self.playerRect =self.playerList[int(number)]
        return self.playerRect
