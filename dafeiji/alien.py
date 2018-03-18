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
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
       




