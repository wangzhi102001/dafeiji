# -*- coding:utf-8 -*-
import pygame
from setting import Setting
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien


def run_game():
    pygame.init()
    ai_setting = Setting()  # 导入设置
    screen = pygame.display.set_mode((ai_setting.screen_wide, ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")  # 设置屏幕宽度、高度，标题

    ship = Ship(ai_setting, screen)
    
    bullets = Group()
    aliens = Group()

    gf.creat_fleet(ai_setting,screen,aliens,ship)
    
    while True:
        gf.check_event(ai_setting,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_setting, screen, ship,aliens,bullets)


run_game()

