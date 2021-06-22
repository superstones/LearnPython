import pygame
from settings import Settings
import functions as f
from roler import Roler
from ball import Ball
from pygame.sprite import Group
from state import State


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    roler = Roler(settings, screen)
    ball = Ball(settings, screen)
    count = 0
    while True:
        f.check_event(roler)
        check = f.check_cross(screen, roler, ball)
        if check:
            count += 1
            print("你已经接住" + str(count) + "个球啦！再接再厉！")
        elif check == False:
            print("没接住，继续努力！")
        f.update_screen(settings, screen, roler, ball)


run_game()
