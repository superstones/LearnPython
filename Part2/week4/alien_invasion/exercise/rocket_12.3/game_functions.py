import sys

import pygame


def check_keydown_events(event, rocket):
    """响应按键"""
    if event.key == pygame.K_UP:
        rocket.moving_up = True
    if event.key == pygame.K_DOWN:
        rocket.moving_down = True
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = True
    if event.key == pygame.K_LEFT:
        rocket.moving_left = True


def check_keyup_events(event, rocket):
    if event.key == pygame.K_UP:
        rocket.moving_up = False
    if event.key == pygame.K_DOWN:
        rocket.moving_down = False
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = False
    if event.key == pygame.K_LEFT:
        rocket.moving_left = False


def check_events(rocket):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, rocket)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, rocket)


def update_screen(ai_settings, screen, rocket):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    rocket.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()
