#gameclass, will work ass the class that will contain everything
import pygame
from Button import Button
from Player import player
from sys import exit
from Enemies import enemies
from Background import Background
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
    index=0
    player_index = 0
    def __init__(self): #constructor de la clase
        pygame.init()
        self.nivel=1
        self.startScreen=pygame.display.set_mode((600,400))
        self.Screen =1
        pygame.display.set_caption("SpaceInvaders")
        self.background= Background()
        self.enemigos = enemies()
        self.jugador = player()

    def get_font(self,size):  # Returns Press-Start-2P in the desired size
        return pygame.font.Font("Pixeltype.ttf", size)
    def lvlUp(self):
        self.nivel+=1
    #RENDERS------------------------------------------------
    def playerRender(self):
        self.startScreen.blit(self.jugador.getrect(self.player_index),(self.jugador.xmovement ,self.jugador.ymovement))  # ideal config
        self.player_index += 0.1
        if self.player_index > 2:
            self.player_index = 0
    def renderEnemies(self):
        n=0
        h=0
        for i in range(0,9):
            n=0
            for j in range(0,9):
                n+=1
                if self.enemigos.isDead(i,j)==False:
                    self.startScreen.blit(self.enemigos.enemyskinList[int(self.index)].convert_alpha(), (40+40*n +30*self.enemigos.xmovement, 25*h+self.enemigos.ymovement)) #ideal config
                    self.index+=0.1
                    if self.index>2 :
                        self.index=0
            h += 1
    def renderLasers(self):
        self.jugador.lasers.draw(self.startScreen)
        self.enemigos.lasers.draw(self.startScreen)
    #END OF RENDERS------------------------------------------
    #COLLISION CHECKER:
    def collisionCker(self):
        #enemy collision
        #a little bit inneficcient but, i discover the sprite class of pygame later on, so
        #ill have to change everything in order to make it cleaner
        #puedo meter un rectangulo aca , y que checkee con el rectangulo...
        rectangulo = None
        if self.jugador.lasers:
            for laser in self.jugador.lasers:
                n = 0
                h = 0
                for i in range(0, 9):
                    n = 0
                    for j in range(0, 9):
                        n += 1
                        if self.enemigos.isDead(i, j) == False:
                            if laser.rect.collidepoint((40 + 40 * n + 30 * self.enemigos.xmovement, 25 * h + self.enemigos.ymovement)):
                                self.enemigos.deleteEnemy(i,j)
                                laser.kill()
                                break
                    h += 1
    #END OF COLLISION CHECKER.
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
    def play(self):
        print("hola")
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
            self.jugador.updateLaser()
            self.enemigos.updateLasers()
            #end of updates
            #renders
            #self.renderEnemies() #renderiza enemigos
            self.playerRender()
            self.renderLasers()
            self.renderEnemies()
            #renders end
            #Collisions
            self.collisionCker()
            #end of collisions
            PLAY_BACK = Button(image=None, pos=(500, 380),
                               text_input="BACK", font=self.get_font(25), base_color="White", hovering_color="Green")
            PLAY_BACK.changeColor(PLAY_MOUSE_POS)
            PLAY_BACK.update(self.startScreen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        self.gameFlag =False
                if event.type == pygame.USEREVENT:
                    self.enemigos.move()
                    self.enemigos.shooting()
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
    def options(self):
        print("xd")
