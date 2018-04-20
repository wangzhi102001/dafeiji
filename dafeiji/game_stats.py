class GameStats():
    """跟踪游戏的统计信息"""
    def __init__(self, ai_setting):
        self.ai_setting = ai_setting
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.ai_setting.ship_limit