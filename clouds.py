import pygame,random,time
from pygame.sprite import Sprite
random.seed(time.time())
class Clouds(Sprite):
    """表示单个云朵类"""

    def __init__(self,ai_settings,screen):
        """初始化云朵的起始位置"""
        super(Clouds,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #加载云朵的图像，并设置其rect的属性
        self.image = pygame.image.load('images/cloud.png')
        self.rect = self.image.get_rect()

        #每多云彩的初始位置
        self.rect.left = random.randint(0,ai_settings.screen_width-self.rect.width)
        self.rect.y = 0 - self.rect.height

        #储存云朵的准确位置
        self.y = float(self.rect.y)
    def update(self):
        """云朵移动"""
        #更新表示云朵位置的小数值
        self.y += self.ai_settings.cloud_speed_factor
        #更新子弹的位置
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image,self.rect)