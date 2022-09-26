import pygame
from player import Player
from settings import *

from src.platform import Platform


class Level:
    def __init__(self):
        # get the display surface
        self.terrain_list = None
        self.player = None
        self.display_surface = pygame.display.get_surface()

        # sprite groups
        self.all_sprites = pygame.sprite.Group()

        self.setup()

    def setup(self):
        self.player = Player((1296, 1080), self.all_sprites)
        self.terrain_list = self.build_terrain_list(100, 100, 64, 64)

    def run(self, dt):
        self.display_surface.fill('black')
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)

    @staticmethod
    def build_terrain_list(x, y, w, h):
        ground_list = pygame.sprite.Group()

        ground = Platform(x, y, w, h, 'platformPack_tile016.png')
        ground_list.add(ground)

        return ground_list

    def platform(self, lvl):
        plat_list = pygame.sprite.Group()
        if lvl == 1:
            plat = Platform(200, SCREEN_WIDTH - 97 - 128, 285, 67, 'platformPack_tile016.png')
            plat_list.add(plat)
            plat = Platform(500, SCREEN_HEIGHT - 97 - 320, 197, 54, 'platformPack_tile016.png')
            plat_list.add(plat)
        if lvl == 2:
            print("Level " + str(lvl))

        return plat_list
