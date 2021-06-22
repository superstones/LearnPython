import pygame
import sys
from random import randint


def update_screen(settings, screen, roler, ball):
    screen.fill(settings.bg_color)
    create_ball(ball)
    create_roler(roler)
    pygame.display.flip()


def create_roler(roler):
    roler.blitme()
    roler.update()


def create_ball(ball):
    ball.blitme()
    ball.update()


def check_cross(screen, roler, ball):
    if pygame.sprite.collide_mask(roler, ball):
        ball.rect.x = randint(0, (screen.get_rect().width - ball.rect.x))
        ball.rect.y = 50
        create_ball(ball)
        return True
    elif ball.rect.top >= screen.get_rect().bottom:
        ball.rect.x = randint(0, (screen.get_rect().width - ball.rect.x))
        ball.rect.y = 50
        return False


def check_event(roler):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            check_ket_down(event, roler)
        elif event.type == pygame.KEYUP:
            check_ket_up(event, roler)


def check_ket_down(event, roler):
    if event.key == pygame.K_RIGHT:
        roler.moving_right = True
    if event.key == pygame.K_LEFT:
        roler.moving_left = True


def check_ket_up(event, roler):
    if event.key == pygame.K_RIGHT:
        roler.moving_right = False
    if event.key == pygame.K_LEFT:
        roler.moving_left = False


def collision(game, ball, stats):
    for b in ball:
        if b.check_edge():
            ball.remove(b)
            if stats.balls_left < 3:
                stats.balls_left += 1
                stats.prep_left()
        if stats.balls_left == 3:
            stats.game_active = False
    collisions = pygame.sprite.groupcollide(game, ball, False, True)
