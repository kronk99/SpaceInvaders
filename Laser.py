import pygame
class Laser(pygame.sprite.Sprite):
    def __init__(self, pos , speed ,color):
        super().__init__()
        self.image = pygame.Surface((4,20))
        self.image.fill(color)
        self.rect =self.image.get_rect(center=pos)
        self.speedo = speed
    def update(self ):
        self.rect.y +=self.speedo
        self.destroy()# for cleaning purposes

    def destroy(self): #memory management
        if self.rect.y < -10 or self.rect.y > 650:
            self.kill()


