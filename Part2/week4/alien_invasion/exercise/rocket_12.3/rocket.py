import sys
import pygame
import game_functions as gf
from settings import Settings
from rocket_roler import Rocket


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Rocket")
    # 创建一个角色
    rocket = Rocket(ai_settings, screen)

    while True:
        # 监视键盘和鼠标事件
        gf.check_events(rocket)
        rocket.update()
        # 每次循环时都重绘屏幕
        gf.update_screen(ai_settings, screen, rocket)


run_game()
