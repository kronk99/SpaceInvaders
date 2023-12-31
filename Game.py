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
from Smasher import smasher
from xmlManager import xmlManager
class Game:
    # private: this is put bc c++ or java sintax #
    #flags used to change scenes
    runflag = False
    scoreFlag = False
    gameFlag =False
    lvlupFLAG= False
    #pygame screen stuff
    Screen = 0
    startScreen = None
    clock = pygame.time.Clock()
    #background
    background = None
    #level atribute
    nivel = None
    #player:
    jugador = None #player instance
    jugadorGroup = None #player group (for animation purposes)
    index = 0 #animation purpuses
    player_index = 0 #animation purposes
    #enemies:
    enemigos = None
    enemyRow= None
    enemyColum = None
    enemyLasers = None #sprite group of laser objects
    smashers=None
    # enemy renders
    enemySkin1 = pygame.image.load("enemy1.png")
    enemySkin2 = pygame.image.load("enemy2.png")
    enemySkin3 = pygame.image.load("enemy3.png")
    enemyskinList = [enemySkin1, enemySkin2, enemySkin3]
    #extra instances
    health=None
    score = None
    smasherSpawnCount = None
    userName= None
    userName_Rect=None
    #music related
    explotionsound = None
    laserSound = None
    xmlMnger = None

    def __init__(self): #constructor de la clase
        pygame.init()
        #screen config
        self.startScreen=pygame.display.set_mode((600,400))
        self.Screen =1
        pygame.display.set_caption("SpaceInvaders")
        self.background= Background()
        #player and enemy assingment
        self.enemigos = pygame.sprite.Group()
        self.smashers=pygame.sprite.Group()
        self.jugador = player()
        self.nivel = 0
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
        #sound related stuff:
        self.explotionsound = pygame.mixer.Sound("explosion.wav")
        self.explotionsound.set_volume(0.2)
        self.laserSound =pygame.mixer.Sound("laser.wav")
        self.laserSound.set_volume(0.1)
        self.scoreFlag=False
        self.smasherSpawnCount=0
        self.xmlMnger = xmlManager()
        self.userName=''
        self.userName_Rect = pygame.Rect(230,300,100,25)



    def get_font(self,size):  # Returns Press-Start-2P in the desired size
        return pygame.font.Font("Pixeltype.ttf", size)
    #SETUP ---------------------------------------
    def alien_setup(self, x_distance=50, y_distance=-50, x_offset=45, y_offset=25):
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
    def smasherSpawn(self):
        self.smasherSpawnCount+=1
        #inneficient af but works
        if self.smasherSpawnCount ==9 and self.nivel==1:
            self.smashers.add(smasher())
            self.smasherSpawnCount=0
        elif self.smasherSpawnCount ==7 and self.nivel==2:
            self.smashers.add(smasher())
            self.smasherSpawnCount=0
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
                    self.explotionsound.play(0)
        #alien laser collision
        if self.enemyLasers:
            for laser in self.enemyLasers:
                if pygame.sprite.spritecollide(laser, self.jugadorGroup,False):
                    print("holaxd")
                    #inneficient af , but its for patch up things purposes
                    vida_list = self.health.sprites()
                    if vida_list: #if the list is not empty
                        vida_list[0].update() #unless
                        laser.kill() #cleaning purposess
                        #print("menosvida")
                        self.explotionsound.play(0)
        if self.smashers:
            for smasher in self.smashers:
                if pygame.sprite.spritecollide(smasher, self.jugadorGroup,False):
                    print("holaxd")
                    #inneficient af , but its for patch up things purposes
                    vida_list = self.health.sprites()
                    if vida_list: #if the list is not empty
                        vida_list[0].update() #unless
                        smasher.kill() #cleaning purposess
                        #print("menosvida")
                        self.explotionsound.play(0)
    #END OF COLLISION CHECKER.
    #UPDATES--------------------------------------------------------
    def winCondition(self):
        #this is the win condition , trows you the you win screen
        if not self.enemigos.sprites() and self.nivel==2 or len(self.health.sprites())==0:
            #the game ins entering the wincon need to fix that
            self.nivel=0
            self.gameFlag=False
            self.scoreFlag =True
            self.xmlMnger.updateScore(self.score.actualScore ,self.userName)
            #cleaning purposes
            self.cleanAll()
            #on here i need to save the current store in the xml document, before cleaning all
        #this is the next level screen, throws you the click to next level screen
        if not self.enemigos.sprites():
            self.lvlupFLAG =True
            self.gameFlag=False
            for laser in self.jugador.lasers:
                laser.kill()
            #delete all things here too


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
    def cleanAll(self):
        for enemigo in self.enemigos:
            enemigo.kill()
        for laser in self.jugador.lasers:
            laser.kill()
        for eLaser in self.enemyLasers:
            eLaser.kill()
        self.nivel = 0
        for health in self.health:
            health.kill()
        self.score=0
    #END OF UPDATES.
#START SCREEN LOOOP ***************************************************************
    def startscreen(self):
        self.startScreen.fill("black")
        #self.userName = 'hola'
        pygame.draw.rect(self.startScreen,(255,255,255,255),self.userName_Rect,2)
        player_name_surf = self.get_font(50).render(self.userName, True, (255, 155, 25, 55))
        self.startScreen.blit(player_name_surf, (235, 300))
        self.userName_Rect.w = player_name_surf.get_width()+10
        #self.userName_Rect.h = player_name_surf.get_height() - 10
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = self.get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(300, 100))
        USERNAME_TEXT = self.get_font(50).render("Write your name", True, "lightblue")
        USERNAME_RECT = MENU_TEXT.get_rect(center=(330, 300))
        PLAY_BUTTON = Button(image=None, pos=(300, 150),
                             text_input="PLAY", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=None, pos=(300, 200),
                                text_input="OPTIONS", font=self.get_font(75), base_color="#d7fcd4",
                                hovering_color="White")
        QUIT_BUTTON = Button(image=None, pos=(300, 250),
                             text_input="QUIT", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")

        self.startScreen.blit(MENU_TEXT, MENU_RECT)
        self.startScreen.blit(MENU_TEXT, MENU_RECT)
        self.startScreen.blit(USERNAME_TEXT, USERNAME_RECT)
        #self.victoryScene() idk if this has to go or not, check later
        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(self.startScreen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.Screen = 0
                exit()
            if event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.userName =self.userName[:-1]
                else:
                    self.userName += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    self.gameFlag = True
                    self.runflag=False
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    self.options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    self.Screen = 0
                    exit()
        pygame.display.update()  # actualiza el display ,deberia de ir en el metodo update.
        self.clock.tick(60)  # maximum frame rate

#GAME LOOP ****************************************************************
    #*********************************
    def loadGame(self):
        self.runflag =True #this flag is for the startscreen
        while self.Screen !=0: #this flag is for the start screen
            if self.runflag:
                self.startscreen()
            elif self.gameFlag==True: #this flag is for the game screen
                if self.nivel==0:
                    self.level1()
                elif self.nivel==1:
                    self.level2()
                else:
                    self.level3()

            elif self.lvlupFLAG==True:
                self.lvlupScene()
            else:
                self.victoryScene()
    def level1(self):
        print("hola")
        # SETUPS
        self.alien_setup()
        self.healthsetup()
        # need a restart all here.
        while self.gameFlag == True:
            PLAY_MOUSE_POS = pygame.mouse.get_pos()
            self.startScreen.fill("black")
            self.background.topbg1 += 1
            self.background.topbg2 += 1
            self.background.checklimit()
            self.startScreen.blit(self.background.bg2, (0, self.background.topbg2))
            self.startScreen.blit(self.background.bg, (0, self.background.topbg1))
            # updates
            self.updateLasers()
            self.winCondition()
            self.jugador.gravity()
            # end of updates
            # renders
            #self.smashers.draw(self.startScreen)  # TEST
            self.lifeRender()
            self.playerRender()
            self.renderLasers()
            self.renderScore()  # renders the score
            self.renderEnemies()
            # renders end
            # Collisions
            self.collisionCker()
            # end of collisions
            PLAY_BACK = Button(image=None, pos=(500, 380),
                               text_input="BACK", font=self.get_font(25), base_color="White", hovering_color="Green")
            PLAY_BACK.changeColor(PLAY_MOUSE_POS)
            PLAY_BACK.update(self.startScreen)
            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        self.gameFlag = False
                        self.runflag=True
                        self.xmlMnger.updateScore(self.score.actualScore , self.userName)
                        self.cleanAll()
                if event.type == pygame.USEREVENT:  # the cound time event is in enemies class
                    self.enemigos.update()
                    self.shooting()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.jugador.shoot()
                        self.laserSound.play(0)
                    if event.key == pygame.K_w:
                        self.jugador.jump()
                    if event.key == pygame.K_a:
                        self.jugador.checkLimits(-30)
                    if event.key == pygame.K_d:
                        self.jugador.checkLimits(30)
            pygame.display.update()
            self.clock.tick(60)
            # end of events
    def level2(self):
        print("level2")
        # SETUPS
        self.alien_setup()
        # need a restart all here.
        while self.gameFlag == True:
            PLAY_MOUSE_POS = pygame.mouse.get_pos()
            self.startScreen.fill("black")
            self.background.topbg1 += 1
            self.background.topbg2 += 1
            self.background.checklimit()
            self.startScreen.blit(self.background.bg2, (0, self.background.topbg2))
            self.startScreen.blit(self.background.bg, (0, self.background.topbg1))
            # updates
            self.updateLasers()
            self.winCondition()
            self.smashers.update()
            self.jugador.gravity()
            # end of updates
            # renders
            self.smashers.draw(self.startScreen)  # TEST
            self.lifeRender()
            self.playerRender()
            self.renderLasers()
            self.renderScore()  # renders the score
            self.renderEnemies()
            # renders end
            # Collisions
            self.collisionCker()
            # end of collisions
            PLAY_BACK = Button(image=None, pos=(500, 380),
                               text_input="BACK", font=self.get_font(25), base_color="White", hovering_color="Green")
            PLAY_BACK.changeColor(PLAY_MOUSE_POS)
            PLAY_BACK.update(self.startScreen)
            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        self.gameFlag = False
                        self.runflag = True
                        self.xmlMnger.updateScore(self.score.actualScore,self.userName)
                        self.cleanAll()
                if event.type == pygame.USEREVENT:  # the cound time event is in enemies class
                    self.enemigos.update()
                    self.shooting()
                    self.smasherSpawn()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.jugador.shoot()
                        self.laserSound.play(0)
                    if event.key == pygame.K_w:
                        self.jugador.jump()
                    if event.key == pygame.K_a:
                        self.jugador.checkLimits(-30)
                    if event.key == pygame.K_d:
                        self.jugador.checkLimits(30)
            pygame.display.update()
            self.clock.tick(60)
    def level3(self):
        print("level2")
        # SETUPS
        self.alien_setup()
        # need a restart all here.
        while self.gameFlag == True:
            PLAY_MOUSE_POS = pygame.mouse.get_pos()
            self.startScreen.fill("black")
            self.background.topbg1 += 1
            self.background.topbg2 += 1
            self.background.checklimit()
            self.startScreen.blit(self.background.bg2, (0, self.background.topbg2))
            self.startScreen.blit(self.background.bg, (0, self.background.topbg1))
            # updates
            self.updateLasers()
            self.winCondition()
            self.smashers.update()
            self.jugador.gravity()
            # end of updates
            # renders
            self.smashers.draw(self.startScreen)  # TEST
            self.lifeRender()
            self.playerRender()
            self.renderLasers()
            self.renderScore()  # renders the score
            self.renderEnemies()
            # renders end
            # Collisions
            self.collisionCker()
            # end of collisions
            PLAY_BACK = Button(image=None, pos=(500, 380),
                               text_input="BACK", font=self.get_font(25), base_color="White", hovering_color="Green")
            PLAY_BACK.changeColor(PLAY_MOUSE_POS)
            PLAY_BACK.update(self.startScreen)
            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        self.gameFlag = False
                        self.runflag = True
                        self.xmlMnger.updateScore(self.score.actualScore,self.userName)
                        self.cleanAll()
                if event.type == pygame.USEREVENT:  # the cound time event is in enemies class
                    self.enemigos.update()
                    self.shooting()
                    self.smasherSpawn()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.jugador.shoot()
                        self.laserSound.play(0)
                    if event.key == pygame.K_w:
                        self.jugador.jump()
                    if event.key == pygame.K_a:
                        self.jugador.checkLimits(-30)
                    if event.key == pygame.K_d:
                        self.jugador.checkLimits(30)
            pygame.display.update()
            self.clock.tick(60)
    def options(self):
        self.scoreFlag = True
        self.victoryScene()
    def victoryScene(self):
        if self.scoreFlag==True:
            print("entre aca papi")
            while self.scoreFlag ==True:
                self.startScreen.fill("black")
                _MOUSE_POS = pygame.mouse.get_pos()
                #change the score to you win or you lose with a variable later on
                MENU_TEXT = self.get_font(100).render("High Scores!", True, "lightblue")

                MENU_RECT = MENU_TEXT.get_rect(center=(200, 50))
                player1text = self.get_font(35).render("-"+self.xmlMnger.getplayerName(0)+"...", True, "magenta")
                player1rect = player1text.get_rect(center =(200 , 125))
                player2text = self.get_font(35).render("-"+self.xmlMnger.getplayerName(1)+"...", True, "red")
                player2rect = player1text.get_rect(center=(200, 145))
                player3text = self.get_font(35).render("-"+self.xmlMnger.getplayerName(2)+"...", True, "purple")
                player3rect = player1text.get_rect(center=(200, 165))
                player4text = self.get_font(35).render("-"+self.xmlMnger.getplayerName(3)+"...", True, "yellow")
                player4rect = player1text.get_rect(center=(200, 185))
                player5text = self.get_font(35).render("-"+self.xmlMnger.getplayerName(4)+"...", True, "green")
                player5rect = player1text.get_rect(center=(200, 205))
                player1Score = self.get_font(35).render("-" + self.xmlMnger.getplayerScore(1) + "...", True, "magenta")
                player1rect1 = player1text.get_rect(center=(350, 125))
                player2Score = self.get_font(35).render("-" + self.xmlMnger.getplayerScore(2) + "...", True, "magenta")
                player2rect1 = player1text.get_rect(center=(350, 145))
                player3Score = self.get_font(35).render("-" + self.xmlMnger.getplayerScore(3) + "...", True, "magenta")
                player3rect1 = player1text.get_rect(center=(350, 165))
                player4Score = self.get_font(35).render("-" + self.xmlMnger.getplayerScore(4) + "...", True, "magenta")
                player4rect1 = player1text.get_rect(center=(350, 185))
                player5Score = self.get_font(35).render("-" + self.xmlMnger.getplayerScore(5) + "...", True, "magenta")
                player5rect1 = player1text.get_rect(center=(350, 205))
                RETURN_BUTTON = Button(image=None, pos=(300, 350),
                                     text_input="return", font=self.get_font(35), base_color="#d7fcd4",
                                     hovering_color="White")
                #paint on screen
                self.startScreen.blit(MENU_TEXT, MENU_RECT)
                self.startScreen.blit(player1text, player1rect)
                self.startScreen.blit(player2text, player2rect)
                self.startScreen.blit(player3text, player3rect)
                self.startScreen.blit(player4text, player4rect)
                self.startScreen.blit(player5text, player5rect)
                self.startScreen.blit(player1Score, player1rect1)
                self.startScreen.blit(player2Score, player2rect1)
                self.startScreen.blit(player3Score, player3rect1)
                self.startScreen.blit(player4Score, player4rect1)
                self.startScreen.blit(player5Score, player5rect1)
                #end of paint on screen
                RETURN_BUTTON.update(self.startScreen)
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if RETURN_BUTTON.checkForInput(_MOUSE_POS):
                            self.scoreFlag=False
                            self.runflag=True
                            #here i need to reset everything
                pygame.display.update()
                self.clock.tick(60)
    def lvlupScene(self): #transition screen , to lvl up and go next level
        #needs a end game button if the player wants that
        if self.lvlupFLAG==True:
            while self.lvlupFLAG ==True:
                self.startScreen.fill("black")
                _MOUSE_POS = pygame.mouse.get_pos()
                #change the score to you win or you lose with a variable later on
                MENU_TEXT = self.get_font(30).render("Excelente, click para el siguiente nivel", True, "#b68f40")
                MENU_RECT = MENU_TEXT.get_rect(center=(300, 100))
                RETURN_BUTTON = Button(image=None, pos=(300, 350),
                                     text_input="next level", font=self.get_font(35), base_color="#d7fcd4",
                                     hovering_color="White")
                self.startScreen.blit(MENU_TEXT, MENU_RECT)
                RETURN_BUTTON.update(self.startScreen)
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if RETURN_BUTTON.checkForInput(_MOUSE_POS):
                            self.lvlupFLAG=False
                            self.gameFlag =True
                            self.nivel += 1
                pygame.display.update()
                self.clock.tick(60)