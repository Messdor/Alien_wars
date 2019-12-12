#bullet.py
import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    """对飞船发射子弹管理的类"""

    def __init__(self,ai_settings,screen,ship):
        """在飞船所处的位置创建一个子弹"""
        super().__init__()
        #可以使用 spuer().__init__() 代替
        self.screen = screen

        #在（0,0）处创建一个表示子弹的矩形，在设置它的位置
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #储存用浮点数表示的子弹位置
        self.y = float(self.rect.y)

        #子弹的颜色和速度
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """子弹移动"""
        #更新表示子弹位置的小数值
        self.y -= self.speed_factor
        #更新子弹的rect的位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)