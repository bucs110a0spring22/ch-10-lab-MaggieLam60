import sys
import pygame
import random
from src import hero
from src import enemy
from src import bolt


class Controller:
    def __init__(self, width=640, height=480):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill((250, 250, 250))  # set the background to white
        pygame.font.init()  # you have to call this at the start, if you want to use this module.
        pygame.key.set_repeat(1, 50)  # initialize a held keey to act as repeated key strikes
        """Load the sprites that we need"""

        self.enemies = pygame.sprite.Group()
        num_enemies = 3
        for i in range(num_enemies):
            x = random.randrange(100, 400)
            y = random.randrange(100, 400)
            self.enemies.add(enemy.Enemy("Boogie", x, y, 'assets/enemy.png'))
        self.hero = hero.Hero("Conan", 50, 80, "assets/hero.png")
        self.all_sprites = pygame.sprite.Group((self.hero,) + tuple(self.enemies))
        self.bolt = None
        self.state = "GAME"

    def mainLoop(self):
        while True:
            if(self.state == "GAME"):
                self.gameLoop()
            elif(self.state == "GAMEOVER"):
                self.gameOver()

    def gameLoop(self):
        while self.state == "GAME":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_UP):
                        self.hero.move_up()
                    elif(event.key == pygame.K_DOWN):
                        self.hero.move_down()
                    elif(event.key == pygame.K_LEFT):
                        self.hero.move_left()
                    elif(event.key == pygame.K_RIGHT):
                        self.hero.move_right()
                    elif(event.key == pygame.K_SPACE):
                      if self.bolt == None:
                        self.fire(self.hero)

            # check for collisions
            fights = pygame.sprite.spritecollide(self.hero, self.enemies, True)
            if(fights):
                for e in fights:
                    if(self.hero.fight(e)):
                        e.kill()
                        self.background.fill((250, 250, 250))
                    else:
                        self.background.fill((250, 0, 0))
                        self.enemies.add(e)


                      
            if self.bolt != None:  
              shots = pygame.sprite.spritecollide(self.bolt,self.enemies, True)
              if shots:
                for e in shots:
                  e.kill()
                  self.background.fill((250, 250, 250))
  
              # redraw the entire screen
            self.enemies.update()
            
            if self.bolt != None:
              self.bolt.update()
              if self.bolt.distance > 1000:
                self.bolt = None
            self.screen.blit(self.background, (0, 0))
            if(self.hero.health == 0):
                self.state = "GAMEOVER"
              
            self.all_sprites.draw(self.screen)
          
            if self.bolt != None:
              pygame.sprite.Group((self.bolt,)).draw(self.screen)

            # update the screen
            pygame.display.flip()
'''
Added- 
Bolts and bolt collisions
space button shoots banana
collision kill enemies 

'''


  
    def fire(self,hero):
      self.bolt = bolt.Bolt(hero.rect.x + 5,hero.rect.y,"assets/banana.png")
      ''' 
      description: fires the banana, 
      arg(self,hero), 
      returns: none'''

    def gameOver(self):
        self.hero.kill()
        myfont = pygame.font.SysFont(None, 30)
        message = myfont.render('Game Over', False, (0, 0, 0))
        self.screen.blit(message, (self.width / 2, self.height / 2))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
