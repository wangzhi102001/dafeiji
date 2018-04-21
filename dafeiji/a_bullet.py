import pygame
from pygame.sprite import Sprite
import math
import random
from bullet import Bullet

class a_bullet(Bullet):
    """外星人子弹"""
    
    def __init__(self, ai_setting, screen, alien):
        
        super(Bullet,self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, ai_setting.alien_bullet_width,
                                ai_setting.alien_bullet_height)
        self.rect.centerx = alien.rect.centerx
        self.rect.y = alien.rect.centery
        #self.rect.top = screen.get_rect().centery
        self.speed_factor = ai_setting.alien_bullet_speed

        self.b = float(self.rect.y)
        self.a = float(self.rect.x)
        self.color = ai_setting.alien_bullet_color
        self.speed_factor = ai_setting.alien_bullet_speed

    def update(self):
        self.b += self.speed_factor
        self.rect.y = self.b

        self.rect.x = self.a
        self.rect.y = self.b


    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


