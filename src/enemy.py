import pygame
import random
#model
class Enemy(pygame.sprite.Sprite):
    def __init__(self, name, x, y, img_file):
        #initialize all the Sprite functionality
        pygame.sprite.Sprite.__init__(self)

        #The following two attributes must be called image and rect
        #pygame assumes you have intitialized these values
        #and uses them to update the screen

        #create surface object image
        self.image = pygame.image.load(img_file).convert_alpha()
        #get the rectangle for positioning
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #set other attributes
        self.name = name + str(id(self))
        self.speed = 2

    def update(self):
      randNum = random.randint(-1,1)
      randNum2 = random.randint(-1,1)
      self.rect.x += randNum
      self.rect.y += randNum2
        # print("'Update me,' says " + self.name)
      '''
      description: updates movement of the hero, randomly x and y
      arg= self
      return = none
      '''
