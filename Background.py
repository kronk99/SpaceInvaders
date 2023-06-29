import pygame
class Background:
    bg = pygame.image.load("Background1.png")
    bg2 =pygame.image.load("Background2.png")
    topbg1 = None
    topbg2=None

    def __init__(self):
        self.topbg1=0
        self.topbg2=-450
    def checklimit(self):
        if self.topbg1 ==400:
            self.topbg1=-450
        if self.topbg2==400:
            self.topbg2 =-450