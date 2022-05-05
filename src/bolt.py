import pygame

class Bolt(pygame.sprite.Sprite):
    def __init__(self, x, y, sprite):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(sprite).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.distance = 0
    '''
description: makes the sprite bolt
arg= self, x, y , sprite
returns= none

'''

    def update(self):
      self.distance += 15
      self.rect.x += 15
    '''
description= updates the distance
arg= (self)
return= none
'''
    