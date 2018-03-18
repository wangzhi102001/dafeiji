# -*- coding:utf-8 -*-
import pygame
from setting import Setting
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()
    ai_setting = Setting()  # 导入设置
    screen = pygame.display.set_mode(
        (ai_setting.screen_wide, ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")  # 设置屏幕宽度、高度，标题

    ship = Ship(ai_setting, screen)

    while True:
        gf.check_event(ship)
        ship.update()
        gf.update_screen(ai_setting, screen, ship)


run_game()

