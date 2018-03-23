import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """外星人"""
    def __init__(self, ai_setting, screen):
        
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_setting = ai_setting
        self.image = pygame.image.load("images/ufo1.bmp")
        self.rect = self.image.get_rect()
        #self.rect.x = self.rect.width

        #self.rect.y = self.rect.height
        self.rect.x = 0
        self.rect.y = 0
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image,self.rect)

       




