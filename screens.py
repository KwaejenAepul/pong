import pygame

class TitleScreen:
    def __init__(self):
        self.title = "PONG"
        self.font = pygame.font.SysFont('Hack', 30)
        self.text = self.font.render("Play", True, (255,255,255))

    def update(self, selection_cursor):
        if selection_cursor == 0:
            self.text = self.font.render("Play", True, (255,255,255))
        elif selection_cursor == 1:
            self.text = self.font.render("Quit", True, (255,255,255))


    def selection_rect(self):
        pass

class GameScreen:
    def __init__(self, player, ai, WIDTH, HEIGHT):
        self.playerscore = player.score
        self.aiscore = ai.score
        self.midrect = pygame.Rect((WIDTH/2 - 5,0),(10, HEIGHT) ) #gotta fix this shiz

    def displayscore(self):
        font = pygame.font.SysFont('Hack', 30)
        displayPlayerScore = font.render(f"{self.playerscore}", True, (160,160,160))
        displayerAiScore = font.render(f"{self.aiscore}", True, (160,160,160))
        return displayPlayerScore, displayerAiScore

class WinScreen:
    def __init__(self, player, ai):
        self.playerscore = player.score
        self.aiscore = ai.score
        self.title = "YOU WON"
        self.font = pygame.font.SysFont('Hack', 30)
        self.text = self.font.render("Play", True, (255,255,255))

    def update(self, selection_cursor):
        if selection_cursor == 0:
            self.text = self.font.render("Play", True, (255,255,255))
        elif selection_cursor == 1:
            self.text = self.font.render("Quit", True, (255,255,255)) 

class GameOverScreen:
    def __init__(self, player, ai):
        self.playerscore = player.score
        self.aiscore = ai.score
        self.title = "YOU LOST"
        self.font = pygame.font.SysFont('Hack', 30)
        self.text = self.font.render("Play", True, (255,255,255))

    def update(self, selection_cursor):
        if selection_cursor == 0:
            self.text = self.font.render("Play", True, (255,255,255))
        elif selection_cursor == 1:
            self.text = self.font.render("Quit", True, (255,255,255))

