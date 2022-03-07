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

    def update(self, height, player, ai):
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
        self.score = 0


class Player(paddle):
    def __init__(self, x, y):
        paddle.__init__(self, x, y)
        self.score = 0

    def update(self, HEIGHT):
        input = pygame.key.get_pressed()
        if input[K_DOWN]:
            if self.y + self.height + self.speed < HEIGHT:
                self.y += self.speed
        if input[K_UP]:
            if self.y + self.speed > 0:
                self.y -= self.speed


class Ai(paddle):
    def __init__(self, x, y):
        paddle.__init__(self, x, y)
        self.score = 0


    def monado(self, bally, ballx, ballspeed, ballsize, direction, HEIGHT):
        i = 0
        direction = direction
        while True:
            if bally >= HEIGHT - ballsize and direction == ballspeed:
                direction = - ballspeed
            elif bally <= 0 and direction == -ballspeed:
                direction = ballspeed
            if ballx >= self.x:
                break
            ballx += ballspeed
            bally += direction
            i+=1
        return bally

    def update(self, ball, HEIGHT):
        bally = int(ball.y)
        ballx = int(ball.x)
        ballspeed = int(ball.speed)
        ballsize = int(ball.size)
        direction = int(ball.direction_y)
        bally = self.monado(bally, ballx, ballspeed, ballsize, direction, HEIGHT)
        print(bally, ball.y)
        if bally > self.y:
            if self.y + self.height >= HEIGHT:
                pass
            else:
                self.y += self.speed
        if bally <= self.y + (self.height/2):
            self.y -= self.speed


def reset(player, ai, ball, HEIGHT, WIDTH):
    player.y = HEIGHT/2 - 75
    ai.y = HEIGHT/2 - 75
    ball.x = WIDTH/2
    ball.y = HEIGHT/2
