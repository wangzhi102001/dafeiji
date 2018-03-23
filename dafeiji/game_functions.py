
# -*- coding:utf-8 -*-
import pygame
import sys
from bullet import Bullet
from alien import Alien



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
    elif event.key == pygame.K_q:
        sys.exit()


def update_screen(ai_setting, screen, ship,aliens,bullets):
    # 更新屏幕数据
    screen.fill(ai_setting.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    ship.bliteme()
    aliens.draw(screen)

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

def creat_fleet(ai_setting,screen,aliens,ship):
    #创建外星人群
    alien = Alien(ai_setting,screen)
    number_aliens_x = get_number_aliens_x(ai_setting,alien.rect.width)
    number_aliens_y = get_number_aliens_y(ai_setting,alien.rect.height,ship.rect.height)
    #创建第一行外星人
    for row_number in range(number_aliens_y):
        for alien_number in range(number_aliens_x):
            creat_alien(ai_setting,screen,aliens,alien_number,row_number)
       

def get_number_aliens_x(ai_setting,alien_width):
    #获取横向外星人数
    available_space_x = ai_setting.screen_wide - alien_width
    number_aliens_x = int(available_space_x/(1.5*alien_width))
    return number_aliens_x

def get_number_aliens_y(ai_setting,alien_height,ship_height):
    #获取纵向外星人数
    avilable_space_y = ai_setting.screen_height - 3* alien_height
    number_aliens_y = int(avilable_space_y/(1.5*alien_height))
    return number_aliens_y

def creat_alien(ai_setting,screen , aliens, alien_number , rows_number):
    #创建横向外星人
    alien = Alien(ai_setting,screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width + 1.5 * alien_width*alien_number
    alien.y = alien_height + 1.5 * alien.rect.height*rows_number
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)



