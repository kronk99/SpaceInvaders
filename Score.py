import pygame
class score(pygame.sprite.Sprite):
    actualScore=None
    font = None
    score_Rect = None
    surface = None
    def __init__(self):
        super().__init__()
        self.actualScore = 0
        self.font= pygame.font.Font("Pixeltype.ttf" , 20)
        self.surface = self.font.render(f'score: {self.actualScore}',False,'white')
        self.score_Rect = self.surface.get_rect(center = (550, 10))
    def increaseScore(self):
        self.actualScore+=10
        self.surface = self.font.render(f'score: {self.actualScore}', False, 'white')
        self.score_Rect = self.surface.get_rect(center=(550, 10))