# -*- coding:utf-8 -*-
import pygame
from setting import Setting
from pygame.sprite import Sprite


class Ship(Sprite):
    """control the ships in AI games"""

    def __init__(self, ai_setting, screen):
        super(Ship,self).__init__()
        self.screen = screen

        self.image = pygame.image.load('images/ship1.bmp')  # 设置飞船图片
        self.rect = self.image.get_rect()  # 将飞船对象定义为矩形
        self.screen_rect = screen.get_rect()  # 飞船定义位置

        self.rect.centerx = self.screen_rect.centerx  # 飞船水平坐标
        self.rect.bottom = self.screen_rect.bottom  # 飞船底部坐标
        self.ai_setting = ai_setting

        self.center = float(self.rect.centerx)

        self.move_right = False  # 右移开关
        self.move_left = False  # 左移开关

    def bliteme(self):
        # 绘制飞船
        self.screen.blit(self.image, self.rect)

    def update(self):
        # 飞船移动函数，根据移动开关

        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_setting.ship_speed_factor
        if self.move_left and self.rect.left > 0:
            self.center -= self.ai_setting.ship_speed_factor
        self.rect.centerx = self.center

    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx
