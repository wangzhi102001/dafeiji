
# -*- coding:utf-8 -*-
import pygame
import sys


# from ship import Ship
def check_event(ship):
    # 响应鼠标和键盘事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_key_up_events(event, ship)


def check_key_up_events(event, ship):
    # 响应“松开按键”事件
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False


def check_key_down_events(event, ship):
    # 响应“按下按键”事件
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True


def update_screen(ai_setting, screen, ship):
    # 更新屏幕数据
    screen.fill(ai_setting.bg_color)
    ship.bliteme()
    pygame.display.flip()
