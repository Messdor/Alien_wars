#settings.py
class Settings():
    """储存alien_invasion的所有设置的类"""
    def __init__(self):
        """初始化游戏的静态设置"""
        #屏幕设置
        self.screen_width = 830
        self.screen_height = 600
        self.bg_color = (230,230,230)

        #子弹设置
        self.bullet_width = 3
        self.bullet_height =15
        self.bullet_color = 60,60,60
        self.bullet_allowed = 3

        #飞船的设置
        self.ship_limit = 2

        #外星人设置
        self.fleet_drop_speed = 10

        #以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而改变"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        #云朵设置
        self.cloud_speed_factor = 0.2

        #fleet_direction为1表示向右移动，为-1表示向左移动
        self.fleet_direction = 1

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.cloud_speed_factor *= self.speedup_scale