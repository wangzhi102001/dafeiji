
# -*- coding:utf-8 -*-
import pygame
import sys
from bullet import Bullet


# from ship import Ship
def check_event(ai_setting,screen, ship,bullets):
    # 响应鼠标和键盘事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down_events(event, ai_setting,screen, ship,bullets)
        elif event.type == pygame.KEYUP:
            check_key_up_events(event, ship)


def check_key_up_events(event, ship):
    # 响应“松开按键”事件
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False


def check_key_down_events(event, ai_setting,screen, ship,bullets):
    # 响应“按下按键”事件
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_setting,screen,ship,bullets)


def update_screen(ai_setting, screen, ship,bullets):
    # 更新屏幕数据
    screen.fill(ai_setting.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.bliteme()
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)
            #print(len(bullets))

def fire_bullet(ai_setting,screen,ship,bullets):
    if len(bullets)<ai_setting.bullet_allowed:
            new_bullet = Bullet(ai_setting,screen,ship)
            bullets.add(new_bullet)


