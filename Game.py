#gameclass, will work ass the class that will contain everything
import pygame
from Button import Button
from Player import player
from sys import exit
from Enemies import enemy
from Background import Background
from Laser import Laser
from random import choice
from Vida import vida
from Score import score
class Game:
    # private: this is put bc c++ or java sintax #
    runflag = False
    startFlag = False
    gameFlag =False
    Screen = 0
    nivel = None #type int
    startScreen = None
    lvl1Screen = None
    clock = pygame.time.Clock()
    background = None
    enemigos = None
    jugador = None
    jugadorGroup =None
    index=0
    player_index = 0
    enemyRow= None
    enemyColum = None
    enemyLasers = None
    health=None
    score = None
    #enemy renders
    enemySkin1 = pygame.image.load("enemy1.png")
    enemySkin2 = pygame.image.load("enemy2.png")
    enemySkin3 = pygame.image.load("enemy3.png")
    enemyskinList = [enemySkin1, enemySkin2, enemySkin3]
    def __init__(self): #constructor de la clase
        pygame.init()
        #screen config
        self.startScreen=pygame.display.set_mode((600,400))
        self.Screen =1
        pygame.display.set_caption("SpaceInvaders")
        self.background= Background()
        #player and enemy assingment
        self.enemigos = pygame.sprite.Group()
        self.jugador = player()
        self.nivel = 1
        #enemy rows and colums
        self.enemyRow=9
        self.enemyColum=9
        #enemy laser group (collision checking)
        self.enemyLasers=pygame.sprite.Group()
        #player group (for collision checking
        self.jugadorGroup=pygame.sprite.Group()
        self.jugadorGroup.add(self.jugador)
        self.health= pygame.sprite.Group()
        #Score:
        self.score = score()
    def get_font(self,size):  # Returns Press-Start-2P in the desired size
        return pygame.font.Font("Pixeltype.ttf", size)
    def lvlUp(self):
        self.nivel+=1
    #SETUP ---------------------------------------
    def alien_setup(self, x_distance=50, y_distance=-190, x_offset=45, y_offset=25):
        for row_index, row in enumerate(range(self.enemyRow)):
            for col_index, col in enumerate(range(self.enemyColum)):
                x =  x_distance +col_index * x_offset
                y = y_distance +row_index * y_offset

                if row_index == 0:
                    alien_sprite = enemy(x,y)
                elif 1 <= row_index <= 2:
                    alien_sprite = enemy(x,y)
                else:
                    alien_sprite =enemy(x,y)
                self.enemigos.add(alien_sprite)
    def healthsetup(self):
        self.health.add(vida(10, 10))
        self.health.add(vida(10, 30))
        self.health.add(vida(10, 50))
    #END OF SETUP---------------
    #RENDERS------------------------------------------------
    def playerRender(self):
        self.startScreen.blit(self.jugador.getrect(self.player_index),(self.jugador.rect.x ,self.jugador.rect.y))  # ideal config
        self.player_index += 0.1
        if self.player_index > 3:
            self.player_index = 0
    #for rendering enemies
    def renderEnemies(self):
        for enemigo in self.enemigos:
            self.startScreen.blit(self.getenemySkin() , (enemigo.rect.x,enemigo.rect.y))
    def getenemySkin(self):
        return self.enemyskinList[int(self.player_index)]
    #end of enemy rendering
    def lifeRender(self):
        self.health.draw(self.startScreen)
    def renderLasers(self):
        self.jugador.lasers.draw(self.startScreen)
        self.enemyLasers.draw(self.startScreen)
    def renderScore(self):
        self.startScreen.blit(self.score.surface , self.score.score_Rect)
    #END OF RENDERS------------------------------------------
    #COLLISION CHECKER:
    def collisionCker(self):
        #player laser collision with aliens
        if self.jugador.lasers:
            for laser in self.jugador.lasers:
                if pygame.sprite.spritecollide(laser ,self.enemigos,True):
                    laser.kill()
                    self.scoreOne()
        #alien laser collision
        if self.enemyLasers:
            for laser in self.enemyLasers:
                if pygame.sprite.spritecollide(laser, self.jugadorGroup,False):
                    print("holaxd")
                    #inneficient af , but its for patch up things purposes
                    vida_list = self.health.sprites()
                    if vida_list: #if the list is not empty
                        vida_list[0].update() #unless
                        laser.kill()
                        print("menosvida")

    #END OF COLLISION CHECKER.
    #UPDATES--------------------------------------------------------
    def updateLasers(self):
        self.enemyLasers.update()
        self.jugador.updateLaser()
    def scoreOne(self):
        self.score.increaseScore()
    def shooting(self ): #ENEMY SHOOTING
        if self.enemigos.sprites():
            random_alien = choice(self.enemigos.sprites())
            if random_alien.rect.y >0:
                self.enemyLasers.add(Laser((random_alien.rect.x, random_alien.rect.y), +3, "red"))
            #note to self, if the alien chosen is offscreen , then the bullet will be deleted
            #right away ,so that needs improvement , but for the time being , the extra if f
            #fixes it
    #END OF UPDATES.
#START SCREEN LOOOP ***************************************************************
    def run(self):
        while self.Screen !=0:
            self.startScreen.fill("black")
            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = self.get_font(100).render("MAIN MENU", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))

            PLAY_BUTTON = Button(image=None, pos=(400, 150),
                                    text_input="PLAY", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
            OPTIONS_BUTTON = Button(image=None, pos=(400, 200),
                                        text_input="OPTIONS", font=self.get_font(75), base_color="#d7fcd4",
                                        hovering_color="White")
            QUIT_BUTTON = Button( image=None,pos=(400, 250),
                                     text_input="QUIT", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")

            self.startScreen.blit(MENU_TEXT, MENU_RECT)

            for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.startScreen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.Screen = 0
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                           self.gameFlag =True
                           self.play()
                    if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.options()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        self.Screen = 0
                        exit()
            pygame.display.update()  # actualiza el display ,deberia de ir en el metodo update.
            self.clock.tick(60) # maximum frame rate
#GAME LOOP ****************************************************************
    #*********************************
    def play(self):
        print("hola")
        #SETUPS
        self.alien_setup()
        self.healthsetup()
        #need a restart all here.
        while self.gameFlag ==True:
            PLAY_MOUSE_POS = pygame.mouse.get_pos()
            self.startScreen.fill("black")
            self.background.topbg1+=1
            self.background.topbg2+=1
            self.background.checklimit()
            self.startScreen.blit(self.background.bg2,(0,self.background.topbg2))
            self.startScreen.blit(self.background.bg,(0,self.background.topbg1))
            #updates
            self.updateLasers()
            #end of updates
            #renders
            self.lifeRender()
            self.playerRender()
            self.renderLasers()
            self.renderScore() #renders the score
            self.renderEnemies()
            #renders end
            #Collisions
            self.collisionCker()
            #end of collisions
            PLAY_BACK = Button(image=None, pos=(500, 380),
                               text_input="BACK", font=self.get_font(25), base_color="White", hovering_color="Green")
            PLAY_BACK.changeColor(PLAY_MOUSE_POS)
            PLAY_BACK.update(self.startScreen)
            #events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        self.gameFlag =False
                if event.type == pygame.USEREVENT:
                    self.enemigos.update()
                    self.shooting()
                    #self.enemigos.shooting()
                if event.type == pygame.KEYDOWN :
                    if event.key==pygame.K_SPACE:
                        self.jugador.shoot()
                    if event.key ==pygame.K_w:
                        print("jumping")
                    if event.key ==pygame.K_a:
                        self.jugador.checkLimits(-30)
                    if event.key==pygame.K_d:
                        self.jugador.checkLimits(30)
            pygame.display.update()
            self.clock.tick(60)
            #end of events
    def options(self):
        print("xd")
