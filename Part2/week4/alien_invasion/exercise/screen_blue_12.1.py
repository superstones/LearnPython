import sys
import pygame
import game_functions as gf
from settings import Settings
from diva import Diva


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建一个角色
    diva = Diva(screen)

    while True:
        # 监视键盘和鼠标事件
        gf.check_events()
        # 每次循环时都重绘屏幕
        gf.update_screen(ai_settings, screen, diva)
        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_game()
