import pygame
class vida (pygame.sprite.Sprite):
    texture= pygame.image.load("vida.png")
    def __init__(self , x , y):
        super().__init__()
        self.image = self.texture
        self.rect = self.image.get_rect(center = (x,y))
    def update(self):
        self.kill()