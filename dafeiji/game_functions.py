
# -*- coding:utf-8 -*-
import pygame
import sys
import random
from bullet import Bullet
from a_bullet import a_bullet
from alien import Alien
from time import sleep
from ship import Ship



def check_event(ai_setting, sb, screen, stats, play_button, ship, aliens, bullets,bullets_a):
    # 响应鼠标和键盘事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down_events(event, ai_setting, stats,
                                  aliens, sb, screen, ship, bullets,bullets_a)
        elif event.type == pygame.KEYUP:
            check_key_up_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_setting, sb, screen, stats,
                              play_button, ship, aliens, bullets,bullets_a, mouse_x, mouse_y)


def start_game(ai_setting, aliens, bullets,bullets_a, sb, screen, ship, stats):
    pygame.mouse.set_visible(False)
    stats.reset_stats()

    stats.game_active = True
    sb.prep_high_score()
    sb.prep_score()
    sb.prep_level()
    sb.prep_ships()

    aliens.empty()
    bullets.empty()
    bullets_a.empty()

    creat_fleet(ai_setting, screen, aliens, ship)
    ship.center_ship()


def check_play_button(ai_setting, sb, screen, stats, play_button, ship, aliens, bullets, bullets_a,mouse_x, mouse_y):

    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        ai_setting.initialize_dynamic_settings()
        start_game(ai_setting, aliens, bullets,bullets_a, sb, screen, ship, stats)


def check_key_up_events(event, ship):
    # 响应“松开按键”事件
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False


def check_key_down_events(event, ai_setting, stats, aliens, sb, screen, ship, bullets,bullets_a):
    # 响应“按下按键”事件
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_setting, screen, ship, bullets)
    #   alien_fire_bullet(ai_setting,screen,aliens,bullets_a)
    elif event.key == pygame.K_q:
        sys.exit()
    #elif event.key == pygame.K_p:
    #    ai_setting.initialize_dynamic_settings()
    #    start_game(ai_setting, aliens, bullets, sb, screen, ship, stats)


def update_screen(ai_setting, screen, stats, sb, ship, aliens, bullets,bullets_a, play_button):
    # 更新屏幕数据
    screen.fill(ai_setting.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    for bullet in bullets_a.sprites():
        bullet.draw_bullet()

    ship.bliteme()
    aliens.draw(screen)
        
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()


def check_bullet_alien_collisons(ai_setting, aliens, bullets, bullets_a,screen, stats, sb, ship):
    """响应子弹和外星人的碰撞"""
    # 删除发生碰撞的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, ai_setting.bool_a, True)
    if collisions:
        
        choice_aliens = pygame.sprite.Group(random.choices(aliens.sprites(),k=int(len(aliens)*ai_setting.alien_bullet_percent)))
        #for alien in choice_aliens:
        alien_fire_bullet(ai_setting,screen,choice_aliens,bullets_a)  #碰撞后抽取现存外星人一定比例允许外星人射击

        #for bullet in bullets.copy():
        #    make_new_bullet(ai_setting,screen,ship,bullet.rect.centerx,bullet.rect.centery,bullets)  #碰撞后变换角度

        for aliens in collisions.values():
            stats.score += ai_setting.alien_point*len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        bullets.empty()
        ai_setting.increase_speed()  # 升一级
        stats.level += 1
        sb.prep_level()
        creat_fleet(ai_setting, screen,  aliens, ship)

def check_bullet_ship_collisons(ai_setting, aliens, bullets, bullets_a,screen, stats, sb, ship):
    """响应外星人子弹和飞船的碰撞"""
    # 删除发生碰撞的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets_a, pygame.sprite.Group(ship), True, True)
    if collisions:
        ship_hit(ai_setting,stats,sb,screen,ship,aliens,bullets,bullets_a)


def update_bullets(ai_setting, screen, stats, sb, ship, aliens, bullets,bullets_a):
    # 更新子弹数据
    bullets.update()
    bullets_a.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            # print(len(bullets))

    for bullet in bullets_a.copy():
        if bullet.rect.top >=screen.get_rect().bottom:
            bullets_a.remove(bullet)

    check_bullet_alien_collisons(
        ai_setting, aliens, bullets, bullets_a,screen, stats, sb, ship)

    check_bullet_ship_collisons(ai_setting,aliens,bullets,bullets_a,screen,stats,sb,ship)


def fire_bullet(ai_setting, screen, ship, bullets):
    # 发射子弹
    if len(bullets) < ai_setting.bullet_allowed:
        new_bullet = Bullet(ai_setting, screen, ship)
        bullets.add(new_bullet)

def alien_fire_bullet(ai_setting,screen,aliens,bullets_a):
    #外星人发射子弹
    if len(bullets_a)<ai_setting.bullet_alien_allowed:
        for alien in aliens.sprites():
            new_alien_bullet = a_bullet(ai_setting,screen,alien)
            bullets_a.add(new_alien_bullet) 

def creat_fleet(ai_setting, screen, aliens, ship):
    # 创建外星人群
    alien = Alien(ai_setting, screen)
    number_aliens_x = get_number_aliens_x(ai_setting, alien.rect.width)
    number_aliens_y = get_number_aliens_y(
        ai_setting, ship.rect.height, alien.rect.height)
    # 创建第一行外星人
    for row_number in range(number_aliens_y):
        for alien_number in range(number_aliens_x):
            creat_alien(ai_setting, screen, aliens, alien_number, row_number)


def get_number_aliens_x(ai_setting, alien_width):
    # 获取横向外星人数
    available_space_x = ai_setting.screen_wide - (1 * alien_width)
    number_aliens_x = int(available_space_x / (1.5 * alien_width))
    return number_aliens_x


def get_number_aliens_y(ai_setting, ship_height, alien_height):
    # 获取纵向外星人数
    avilable_space_y = ai_setting.screen_height - \
        (3 * alien_height) - ship_height
    number_aliens_y = int(avilable_space_y / (1.5 * alien_height))
    return number_aliens_y


def creat_alien(ai_setting, screen, aliens, alien_number, rows_number):
    # 创建横向外星人
    alien = Alien(ai_setting, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width + 1.5 * alien_width * alien_number
    alien.y = alien_height + 1.5 * alien.rect.height * rows_number
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)


def check_fleet_edges(ai_setting, aliens):
    # 校验外星人是否发生边际碰撞
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_setting, aliens)
            break


def change_fleet_direction(ai_setting, aliens):
    # 改变垂直速度，并调整横向运动方向
    for alien in aliens.sprites():
        alien.rect.y += ai_setting.fleet_drop_speed
    ai_setting.fleet_direction *= -1


def ship_hit(ai_setting, stats,sb, screen, ship, aliens, bullets,bullets_a):
    """响应被外星人撞到的飞船"""
    # 将ship_left减一
    if stats.ships_left > 0:
        stats.ships_left -= 1

        sb.prep_ships()
        # 清除外星人列表和子弹列表
        bullets_a.empty()
        aliens.empty()
        bullets.empty()
        # 创建一群新的外星人，并将飞船放到屏幕底部中央
        creat_fleet(ai_setting, screen, aliens, ship)
        ship.center_ship()
        # 暂停
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_setting, stats, sb,screen, ship, aliens, bullets,bullets_a):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_setting, stats,sb, screen, ship, aliens, bullets,bullets_a)
            break


def update_aliens(ai_setting, stats,sb, screen, ship, aliens, bullets,bullets_a):
    # 更新外星人参数
    check_fleet_edges(ai_setting, aliens)
    aliens.update()
    #for alien in aliens.sprites():
    #    if ai_setting.random_num==1:
    #        alien_fire_bullet(ai_setting,screen,aliens,bullets_a)

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_setting, stats, sb,screen, ship, aliens, bullets,bullets_a)
    check_aliens_bottom(ai_setting, stats, sb,screen, ship, aliens, bullets,bullets_a)


def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def make_new_bullet(ai_setting,screen,ship,centerx,centery,bullets):
    new_bullet = Bullet(ai_setting,screen,ship)
    bullets.add(new_bullet)

    
