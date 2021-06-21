import pygame
from setting import Settings
from rain import Rain
import functions as f
from pygame.sprite import Group


def display():
    """主函数，显示我的雨滴"""
    pygame.init()
    setting = Settings()
    screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))
    pygame.display.set_caption("My Rain")
    rains = Group()
    f.create_rains(setting, screen, rains)
    while True:
        f.check_events()
        screen.fill(setting.bg_color)
        f.change_direction(setting, rains)
        f.update_rains(setting, screen, rains)
        rains.draw(screen)
        pygame.display.flip()


display()
