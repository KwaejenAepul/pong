import pygame
from pygame.constants import K_DOWN, K_UP

class TitleScreen:
    def __init__(self):
        self.title = "PONG"
        self.selection = 0

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_DOWN:
                    self.selection += 1
                if event.key == K_UP:
                    self.selection -= 1

                if self.selection > 1:
                    self.selection = 0
                if self.selection < 0:
                    self.selection = 1

    def selection_rect(self):
        pass

class GameScreen:
    def __init__(self, player, ai):
        self.playerscore = player.score
        self.aiscore = ai.score
        self.midrect = "rect" #gotta fix this shiz

    def displayscore(self):
        font = pygame.font.SysFont('Hack', 30)
        displayPlayerScore = font.render(f"{self.playerscore}", True, (255,0,0))
        displayerAiScore = font.render(f"{self.aiscore}", True, (255,0,0))
        return displayPlayerScore, displayerAiScore

class WinScreen:
    def __init__(self, player, ai):
        self.playerscore = player.score
        self.aiscore = ai.score
        self.title = "YOU WON"

class GameOverScreen:
    def __init__(self, player, ai):
        self.playerscore = player.score
        self.aiscore = ai.score
        self.title = "YOU LOST"
