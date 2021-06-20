import pygame
import sys
from settings import Settings
from pygame.sprite import Group
import functions as f


def display():
    """显示我的星星"""
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("My Stars")
    stars = Group()
    f.create_stars(settings, screen, stars)

    while True:
        f.check_keys()
        f.update_screen(settings, screen, stars)


display()
