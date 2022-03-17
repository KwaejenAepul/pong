import pygame
from pygame.constants import K_DOWN, K_UP

class pong_ball:
    def __init__ (self, x, y, size):
        self.x:int = x
        self.y:int = y
        self.size:int = size
        self.speed:int = 7
        self.direction_x:int = self.speed
        self.direction_y:int = self.speed

    def update(self, height, player, ai):
        if self.x >= ai.x - self.size and self.y in range(int(ai.y), int(ai.y + ai.height)) and self.direction_x > 0:
            self.calc_angle(ai)
            self.direction_x *= -1
        elif self.x <= player.x + player.width and self.y in range(int(player.y), int(player.y + player.height)) and self.direction_x < 0:
            self.calc_angle(player)
            self.direction_x = self.speed
        if self.y >= height - self.size and self.direction_y > 0:
            self.direction_y *= -1
        elif self.y <= 0 and self.direction_y < 0:
            self.direction_y *= -1
        self.x += self.direction_x
        self.y += self.direction_y

    def calc_angle(self, paddle):
        section_size = int(paddle.height/5)
        if self.x in range(paddle.x, int(paddle.x + section_size)):
            self.direction_x = 4
            self.direction_y = -10
        elif self.x in range(paddle.x, int(paddle.x + (section_size*2))):
            self.direction_x = 6
            self.direction_y = -8
        elif self.x in range(paddle.x, int(paddle.x + (section_size*3))):
            self.direction_x = 7
            self.direction_y = 7
        elif self.x in range(paddle.x, int(paddle.x + (section_size*4))):
            self.direction_x = 6
            self.direction_y = 8
        elif self.x in range(paddle.x, int(paddle.x + (section_size*5))):
            self.direction_x = 4
            self.direction_y = 10

#paddle shit
class paddle:
    def __init__(self, x, y):
        self.x:int = x
        self.y:int = y
        self.width:int = 20
        self.height:int = 150
        self.speed:int = 5

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

    #unbeatable ai part
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
