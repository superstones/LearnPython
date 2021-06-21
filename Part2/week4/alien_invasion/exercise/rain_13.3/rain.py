import pygame
from pygame.sprite import Sprite


class Rain(Sprite):
    """雨滴的类"""

    def __init__(self, settings, screen):
        super(Rain, self).__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load('images/rain.bmp')
        self.rect = self.image.get_rect()
        # self.screen = self.screen.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.top >= screen_rect.bottom:
            return True

    def blitme(self):
        """绘制我的雨滴"""
        self.screen.blit(self.image, self.rect)
