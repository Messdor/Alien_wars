#ship.py
import pygame

class Ship():

    def __init__(self,ai_settings,screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/plane.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将每艘新飞船放置屏幕底部的中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)
        self.top =float(self.rect.top)

        #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        """
        self.moving_up_left =False
        self.moving_up_right = False
        self.moving_down_left =False
        self.moving_down_right = False
        """

    def update(self):
        """根据移动标志调整飞船位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center  -= self.ai_settings.ship_speed_factor
        elif self.moving_up and self.rect.top > 0:
            self.top -= self.ai_settings.ship_speed_factor
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.top += self.ai_settings.ship_speed_factor
        """
        elif self.moving_up_left and self.rect.top > 0 and self.rect.left < self.screen_rect.left:
            self.top -= self.ai_settings.ship_speed_factor
            self.center -= self.ai_settings.ship_speed_factor
        """

        #根据self.center更新rect对象
        self.rect.centerx = self.center
        self.rect.top = self.top

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        """将飞船放置在屏幕底部中央"""
        self.center = self.screen_rect.centerx
        self.top = self.screen_rect.bottom - self.rect.height