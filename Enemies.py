import pygame


class enemies:
    rows, cols = (10, 10)
    # method 2 1st approach
    enemigos = [[0] * cols] * rows
    countenemies = None
    enemySkin = pygame.image.load("enemy1.png")

    def __init__(self):
        for i in range(0, 9):
            for j in range(0, 9):
                self.enemigos[i][j] = 1
        self.countenemies = 20

    def deleteEnemy(self, posx, posy):
        self.enemigos[posy][posx] = 0

    def isDead(self, posx, posy):
        if self.enemigos[posy][posx] != 0:
            return False
        else:
            return True
