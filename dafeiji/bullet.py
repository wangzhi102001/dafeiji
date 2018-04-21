import pygame
from pygame.sprite import Sprite
import math
import random


class Bullet(Sprite):
    """子弹管理"""

    def __init__(self, ai_setting, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, ai_setting.bullet_width,
                                ai_setting.bullet_height)
        self.rect.centerx = ship.rect .centerx
        self.rect.top = ship.rect.top
        #self.rect.top = screen.get_rect().centery

        self.b = float(self.rect.y)
        self.a = float(self.rect.x)

        self.color = ai_setting.bullet_color
        self.speed_factor = ai_setting.bullet_speed_factor

        self.r = float(random.random()*3)  # 旋转半径
        self.r_speed = 2  # 旋转角度
        self.center_x = ship.rect.top  # 旋转中心X坐标
        self.center_y = self.b-self.r  # 旋转中心Y坐标
        self.ran_num = random.randrange(0, 100) % 2

    def update(self):
        #self.y -= self.speed_factor
        #self.rect.y = self.y

        # self.r_speed+=0.03
        # self.center_y-=self.speed_factor
        # self.r+=1
        # self.b=(self.b-self.centery)*math.cos(math.radians(self.r_speed))-(self.a-self.centerx)*math.sin(math.radians(self.r_speed))+self.b
        # self.a=(self.b-self.centery)*math.sin(math.radians(self.r_speed))+(self.a-self.centerx)*math.cos(math.radians(self.r_speed))+self.a
        # self.b=(self.b-self.center_y)*math.cos(math.radians(self.r_speed))-(self.a-self.center_x)*math.sin(math.radians(self.r_speed))+self.center_y
        # self.a=(self.b-self.center_y)*math.sin(math.radians(self.r_speed))+(self.a-self.center_x)*math.cos(math.radians(self.r_speed))+self.center_x

        # if self.ran_num==1:
        #    self.center_y-=self.speed_factor
        #    self.b=(self.b-self.center_y)*math.cos(math.radians(self.r_speed))-(self.a-self.center_x)*math.sin(math.radians(self.r_speed))+self.center_y
        #    self.a=(self.b-self.center_y)*math.sin(math.radians(self.r_speed))+(self.a-self.center_x)*math.cos(math.radians(self.r_speed))+self.center_x
        # else:
        self.b -= self.speed_factor
        self.rect.y = self.b

        self.rect.x = self.a
        self.rect.y = self.b
        # print((self.rect.x,self.rect.y))

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
