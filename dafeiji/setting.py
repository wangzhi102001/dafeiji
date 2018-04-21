# -*- coding:utf-8 -*-
import random


class Setting():
    """Alien_invasion's setting file"""

    def __init__(self):
        self.screen_wide = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3  # 子弹射速
        self.alien_bullet_speed = 0.5 #外星人子弹射速
        self.alien_bullet_width = 5 #外星人子弹宽度
        self.alien_bullet_height = 20 #外星人子弹长度
        self.bullet_width = 5  # 子弹宽度
        self.bullet_height = 20  # 子弹长度
        self.bullet_color = 60, 60, 60  # 子弹颜色、
        self.alien_bullet_color = 242,85,0
        self.bullet_allowed = 5  # 最大子弹允许数量
        self.bullet_alien_allowed = 8   # 最大外星人子弹允许数量
        self.alien_speed_factor = 1  # 外星人移动速度
        self.fleet_drop_speed = 5  # 外星人下移速度
        self.fleet_direction = 1  # fleet_direction为1表示向右移，-1表示向左移
        self.ship_limit = 3  # 飞船复活数量
        self.random_num = random.randrange(0,6)

        self.speedup_scale = 1.1  # 以什么样的速度加快游戏节奏
        self.score_scale = 1.5  # 分数增值
        self.initialize_dynamic_settings()
        self.bool_a = True
        self.alien_bullet_percent = 0.04  #外星人发射子弹比率

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5  # 飞船移动速度
        self.bullet_speed_factor = 3  # 子弹移动速度
        self.alien_speed_factor = 1  # 外星人移动速度
        self.bullet_allowed = 5  # 最大子弹允许数量
        self.bullet_alien_allowed = 1   # 最大外星人子弹允许数量
        self.bullet_width = 5  # 子弹宽度
        self.fleet_direction = 1  # fleet_direction为1表示向右移，-1表示向左移
        self.alien_bullet_speed = 0.5 #外星人子弹射速
        self.ship_level = 1
        self.alien_point = 50
        self.bool_a = True
        self.alien_bullet_percent = 0.04   #第十关开始，外星人开始射击

    def increase_speed(self):
        """升级"""
        self.ship_speed_factor *= self.speedup_scale  #飞船移动速度变化
        self.bullet_speed_factor *= self.speedup_scale #飞船子弹速度变化
        self.alien_speed_factor *= self.speedup_scale  #外星人运动速度变化
        self.bullet_allowed += 1  #飞船子弹最大允许数量增加
        self.bullet_width += 2  #飞船子弹宽度变化
        self.alien_bullet_percent = self.alien_bullet_percent*1.15  #外星人发射子弹比率变化
        
        self.ship_level += 1
        

        if self.ship_level>=10:
            self.alien_bullet_speed *= 1.1 #外星人子弹射速变化
            
            

        if self.ship_level>=8:
            self.bool_a = False   #8级开始子弹开始穿透

        if self.ship_level>=5:
            self.bullet_height+=4    #5级开始子弹开始变宽
            self.bullet_alien_allowed += 1   # 最大外星人子弹允许数量变化

        self.alien_point = int(self.alien_point*self.score_scale)
