import pygame
import random
from pygame.sprite import Sprite


class Alien(Sprite):
    """外星人"""

    def __init__(self, ai_setting, screen):
        super(Alien, self).__init__()
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
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += self.ai_setting.alien_speed_factor * self.ai_setting.fleet_direction
        self.rect.x = self.x
        
        



    def check_edges(self):
        """如果外星人位于屏幕边缘，就返回TRUE"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
