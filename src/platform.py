import pygame
import os

from src.settings import SCREEN_WIDTH

ALPHA = (0, 255, 0)


class Platform(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.image = pygame.Surface((SCREEN_WIDTH * 2, 64))
        self.image.fill('grey')
        self.rect = self.image.get_rect(center=pos)

    # def __init__(self, xloc, yloc, imgw, imgh, img):
    #     pygame.sprite.Sprite.__init__(self)
    #     self.image = pygame.Surface((imgw, imgh))
    #     self.image.fill('grey')
    #     self.rect = self.image.get_rect(center=(xloc, yloc))
        # self.image = pygame.image.load(os.path.join('../assets/environment', img)).convert()
        # self.image.convert_alpha()
        # self.image.set_colorkey(ALPHA)
        # self.rect = self.image.get_rect()
        # self.rect.y = yloc
        # self.rect.x = xloc
