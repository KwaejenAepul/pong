import pygame
from pygame.constants import K_DOWN, K_UP

class pong_ball:
    def __init__ (self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.speed = 7
        self.direction_x = self.speed
        self.direction_y = self.speed

    def update(self, width, height, player, ai):
        width = width
        height = height
        if self.x >= ai.x - self.size and self.y in range(int(ai.y), int(ai.y + ai.height)) and self.direction_x == self.speed:
            self.direction_x = - self.speed
        elif self.x <= player.x + player.width and self.y in range(int(player.y), int(player.y + player.height)) and self.direction_x == -self.speed:
            self.direction_x = self.speed
        if self.y >= height - self.size and self.direction_y == self.speed:
            self.direction_y = - self.speed
        elif self.y <= 0 and self.direction_y == -self.speed:
            self.direction_y = self.speed
        self.x += self.direction_x
        self.y += self.direction_y


class paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 150
        self.speed = 5

    def update(self, HEIGHT):
        input = pygame.key.get_pressed()
        if input[K_DOWN]:
            if self.y + self.height + self.speed < HEIGHT:
                self.y += self.speed
        if input[K_UP]:
            if self.y + self.speed > 0:
                self.y -= self.speed

    def AI_update(self, ball, HEIGHT):
        pass
