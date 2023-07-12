import pygame
import random
class smasher(pygame.sprite.Sprite):
    #note to self, i discovered that with a sprite class , for animation
    #you just need to change the image, not the rectangle itself, so i overcomplicated
    #things with the enemy renders, as well as the player.
    randomSpawn =None
    flag = None #flag for movement, if true moves from left to right, false makes
    #the inverse movement
    #images for animation purposes
    smasher_Air1 =pygame.image.load("Smasher.png")
    smasher_Air2 = pygame.image.load("Smashe2.png")
    smasher_Air3 = pygame.image.load("Smashe3.png")
    smasher_inAir= [smasher_Air1,smasher_Air2,smasher_Air3]
    smasher_Ground1=pygame.image.load("Smasherleft1 Copy.png")
    smasher_Ground2 = pygame.image.load("Smasherleft2.png")
    smasher_Ground3 = pygame.image.load("Smasherleft3.png")
    smasher_Ground = [smasher_Ground1,smasher_Ground2,smasher_Ground3]
    homemadeTimer = None
    smasherIndex=None
    def __init__(self):
        super().__init__()
        self.falling = 0
        self.randomSpawn = random.choice([20 , 560])
        if self.randomSpawn ==20:
            self.flag=True
        else:
            self.flag=False
        self.image = pygame.image.load("Smasher.png")  # this has to be done this way bc of inheritance
        self.rect = self.image.get_rect(center=(self.randomSpawn, -50))
        self.homemadeTimer=0
        self.smasherIndex=0

    def update(self):
        self.movement()
        self.checkmovement()
        self.animation()
    def movement(self): #movement method ,the idea is that the smasher spawns
        #on one side on the screen ,then "run" over the player , like a suicide enemy
        #and deals damage to its health
        if self.rect.y !=350:
            self.rect.y +=1
        else:
            if self.flag ==True:
                self.rect.x +=1
            else:
                self.rect.x -=1
    def checkmovement(self): #switches the tipe of movement, from going down to moving left or right
        if self.rect.x >620 or self.rect.x < -20:
            self.kill()
    def animation(self): #animation of the enemy
        if self.rect.y <= 330:
            self.image = self.smasher_inAir[int(self.smasherIndex)]
            self.smasherIndex += 0.1
            if self.smasherIndex > 3:
                self.smasherIndex = 0
        else:
            self.image=self.smasher_Ground[int(self.smasherIndex)]
            self.smasherIndex += 0.1
            if self.smasherIndex > 3:
                self.smasherIndex = 0