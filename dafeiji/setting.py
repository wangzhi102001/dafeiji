# -*- coding:utf-8 -*-
class Setting():
    """Alien_invasion's setting file"""

    def __init__(self):
        self.screen_wide = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 2
        self.bullet_speed_factor = 2  #子弹射速
        self.bullet_width = 5   #子弹宽度
        self.bullet_height = 30  #子弹长度
        self.bullet_color = 60,60,60  #子弹颜色
        self.bullet_allowed = 5   #最大子弹允许数量

