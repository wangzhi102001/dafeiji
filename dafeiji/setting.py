# -*- coding:utf-8 -*-
class Setting():
    """Alien_invasion's setting file"""

    def __init__(self):
        self.screen_wide = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 3
        self.bullet_speed_factor = 5  #子弹射速
        self.bullet_width = 10   #子弹宽度
        self.bullet_height = 40  #子弹长度
        self.bullet_color = 60,60,60  #子弹颜色
        self.bullet_allowed = 8   #最大子弹允许数量

