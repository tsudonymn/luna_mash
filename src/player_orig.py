import pygame
from settings import *
from support import *

IDLE = '_idle'


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.animations = None
        self.status = 'down_idle'
        self.frame_index = 0

        # general setup
        self.image = pygame.Surface((32, 64))
        self.image.fill('green')
        self.rect = self.image.get_rect(center=pos)

        # movement attributes
        self.direction = pygame.math.Vector2()
        # self.pos = pygame.math.Vector2(self.rect.center)
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200

    def animate(self, dt):
        self.frame_index += 4 * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0

        self.image = self.animations[self.status][int(self.frame_index)]

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = 'up'
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = 'down'
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = 'right'
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = 'left'
        else:
            self.direction.x = 0

    def update_status(self):
        if self.is_idle():
            self.change_status(IDLE)

    # tool use

    def is_moving(self) -> bool:
        return self.direction.magnitude() > 0

    def is_idle(self) -> bool:
        return self.direction.magnitude() == 0

    def move(self, dt):
        # normalizing a vector
        if self.is_moving():
            self.direction = self.direction.normalize()

        # horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x

        # vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

        # print(self.pos.x)
        # print(self.pos.y)

    def update(self, dt):
        self.input()
        self.update_status()

        self.move(dt)
#        self.animate(dt)

    def change_status(self, new_status):
        self.status = self.status.split('_')[0] + new_status
