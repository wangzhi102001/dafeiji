# -*- coding:utf-8 -*-


class Setting():
    """Alien_invasion's setting file"""

    def __init__(self):
        self.screen_wide = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1
        self.bullet_speed_factor = 3  # 子弹射速
        self.bullet_width = 5  # 子弹宽度
        self.bullet_height = 20  # 子弹长度
        self.bullet_color = 60, 60, 60  # 子弹颜色
        self.bullet_allowed = 8  # 最大子弹允许数量
        self.alien_speed_factor = 1  # 外星人移动速度
        self.fleet_drop_speed = 5  # 外星人下移速度
        self.fleet_direction = 1  # fleet_direction为1表示向右移，-1表示向左移
        self.ship_limit = 3  # 飞船复活数量

        self.speedup_scale = 1.1  # 以什么样的速度加快游戏节奏
        self.score_scale = 1.5  # 分数增值
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5  # 飞船移动速度
        self.bullet_speed_factor = 3  # 子弹移动速度
        self.alien_speed_factor = 1  # 外星人移动速度
        self.bullet_allowed = 5  # 最大子弹允许数量
        self.bullet_width = 5  # 子弹宽度
        self.fleet_direction = 1  # fleet_direction为1表示向右移，-1表示向左移
        self.ship_level = 1
        self.alien_point = 50

    def increase_speed(self):
        """升级"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.bullet_allowed += 1
        self.bullet_width += 3
        self.ship_level += 1
        self.alien_point = int(self.alien_point*self.score_scale)
