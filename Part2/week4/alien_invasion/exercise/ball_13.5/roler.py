import pygame


class Roler():
    def __init__(self, settings, screen):
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load('images/roler.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.player_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.player_speed

    def blitme(self):
        self.screen.blit(self.image, self.rect)
