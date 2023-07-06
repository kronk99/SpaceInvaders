import pygame
class enemy(pygame.sprite.Sprite):
    enemySkin1 = pygame.image.load("enemy1.png")
    enemySkin2 = pygame.image.load("enemy2.png")
    enemySkin3 = pygame.image.load("enemy3.png")
    contadorx=None
    movementFlag =None

    def __init__(self, xpos, ypos):
        super().__init__()
        self.countenemies = 20

        self.clock=pygame.time.set_timer(pygame.USEREVENT, 1000,0)
        self.movementFlag =True #if is true, enemies move to right, else , move to left
        self.lasers = pygame.sprite.Group() #shooting of enemies
        self.image=self.enemySkin1 #this has to be done this way bc of inheritance
        self.rect = self.image.get_rect(center=(xpos,ypos))
        self.contadorx= 0


#this method needs to be called update because of polimorfism
    def update(self): #debe de moverse de izquierda a derecha y siempre hacia abajo.
        #bc of how this was programmed , in here i will update the sprite animation and
        #the movement at the same time
        if self.movementFlag ==True:
            if self.contadorx==7: #aritmetica para el movimiento :prueba y error
                self.rect.y+=20
                self.movementFlag =False
            else:
                self.rect.x+=20
                self.contadorx+=1
        else:
            if self.contadorx==0:
                self.rect.y+=20
                self.movementFlag =True
            else:
                self.rect.x-=20
                self.contadorx -= 1
                #print("el contador es:"+str(self.contadorx))




