import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """星星的类"""

    def __init__(self, screen):
        super(Star, self).__init__()
        self.screen = screen

        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()
        self.screen = screen.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def blitme(self):
        """绘制我的星星"""
        self.screen.blit(self.image, self.rect)
