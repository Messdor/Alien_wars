#alien_invasion.py
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #创建Play按钮
    play_button = Button(ai_settings,screen,"Play")

    #创建一艘飞船，一个外星人编组，一个子弹编组,一个云朵组
    ship = Ship(ai_settings,screen)
    aliens = Group()
    bullets = Group()
    clouds = Group()

    #创建一个用于储存游戏统计信息的实例
    stats = GameStats(ai_settings)

    #创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)
    gf.create_fleet_clouds(ai_settings,screen,clouds)

    #开始游戏的主循环
    while True:
        gf.check_events(ai_settings,screen,stats,play_button,ship,aliens,clouds,bullets)
        if stats.game_active:
            ship.update()
            gf.update_clouds(ai_settings,clouds)
            gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)

        gf.update_screen(ai_settings,screen,stats,ship,aliens,bullets,clouds,play_button)

run_game()
