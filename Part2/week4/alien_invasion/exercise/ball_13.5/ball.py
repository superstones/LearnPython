import pygame
from random import randint
from pygame.sprite import Sprite


class Ball():
    def __init__(self, settings, screen):
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load('images/ball.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.x = randint(self.rect.x, (self.screen_rect.width - self.rect.x))

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.rect.y += self.settings.ball_speed
