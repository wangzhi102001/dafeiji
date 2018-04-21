# coding:utf-8
import pygame
from setting import Setting
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard


def run_game():
    pygame.init()
    ai_setting = Setting()  # 导入设置
    screen = pygame.display.set_mode(
        (ai_setting.screen_wide, ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")  # 设置屏幕宽度、高度，标题

    ship = Ship(ai_setting, screen)

    bullets = Group()
    bullets_a = Group()
    aliens = Group()

    gf.creat_fleet(ai_setting, screen, aliens, ship)

    stats = GameStats(ai_setting)
    sb = ScoreBoard(ai_setting, screen, stats)
    play_button = Button(ai_setting, screen, u"PLAY")

    while True:
        gf.check_event(ai_setting, sb, screen, stats,
                       play_button, ship, aliens, bullets,bullets_a)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_setting, screen, stats,
                              sb, ship, aliens, bullets,bullets_a)
            gf.update_aliens(ai_setting, stats, sb,screen, ship, aliens, bullets,bullets_a)

        gf.update_screen(ai_setting, screen, stats, sb,
                         ship, aliens, bullets, bullets_a,play_button)


run_game()
