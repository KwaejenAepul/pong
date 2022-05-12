import objects
import pygame
import screens
from sys import exit
from time import sleep

#game constants no touchywouchy plz uwu
WIDTH = 1500
HEIGHT = 1000
SCREEN_SIZE = WIDTH, HEIGHT

def main():
    #init some shit
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    gamestate = 0
    selection_cursor = 0

    #initialize game objects
    font = pygame.font.SysFont('Hack', 50)
    ball = objects.pong_ball(WIDTH/2, HEIGHT/2, 20)
    player = objects.Player(40,HEIGHT/2 - 75)
    AI = objects.Ai(WIDTH - 50, HEIGHT/2 - 75)
    #initialize different screens
    titlescreen = screens.TitleScreen()
    winscreen = screens.WinScreen(player, AI)
    gameoverscreen = screens.GameOverScreen(player, AI)
    #main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if gamestate < 3:
                        gamestate += 1
                    else:
                        gamestate = 0
                if event.key == pygame.K_DOWN and gamestate != 1:
                    selection_cursor += 1
                if event.key == pygame.K_UP and gamestate != 1:
                    selection_cursor -= 1

                if selection_cursor > 1:
                    selection_cursor = 0
                elif selection_cursor < 0:
                    selection_cursor = 1

        match gamestate:
        #TITLESCREEN
            case 0:
                titlescreen.update(selection_cursor)
                screen.fill((0,0,0))
                title = font.render(f"{titlescreen.title}", True, (255,255,255))
                title_rect = title.get_rect(center=(WIDTH//2, 40))
                text_rect = titlescreen.text.get_rect(center=(WIDTH//2, HEIGHT//2))
                screen.blit(title,title_rect)
                screen.blit(titlescreen.text,text_rect)
        #GAMEPLAY
            case 1:
                gameScreen = screens.GameScreen(player, AI, WIDTH, HEIGHT)
                player.update(HEIGHT)
                AI.update(ball, player, HEIGHT)
                ball.update(HEIGHT, player, AI)
                if ball.x < 0:
                    objects.reset(player, AI, ball, HEIGHT, WIDTH)
                    AI.score += 1
                if ball.x > WIDTH:
                    objects.reset(player, AI, ball, HEIGHT, WIDTH)
                    player.score += 1

                if player.score == 5:
                    gamestate = 3
                elif AI.score == 5:
                    gamestate = 2

                displayPlayerScore, displayAiScore = gameScreen.displayscore()
                AIrect = pygame.Rect((AI.x, AI.y), (AI.width, AI.height))
                playerrect = pygame.Rect((player.x, player.y), (player.width, player.height))
                ballrect = pygame.Rect((ball.x, ball.y), (ball.size, ball.size))
                screen.fill((0,0,0))
                screen.blit(displayPlayerScore, (WIDTH/4,0))
                screen.blit(displayAiScore, (WIDTH - WIDTH/4, 0))
                pygame.draw.rect(screen , (160,160,160), gameScreen.midrect)
                pygame.draw.rect(screen, (255,255,255), ballrect)
                pygame.draw.rect(screen, (255,255,255), playerrect)
                pygame.draw.rect(screen, (255,255,255), AIrect)
        #GAME OVER
            case 2:
                gameoverscreen.update(selection_cursor)
                title = font.render(f"{gameoverscreen.title}", True, (255,255,255))
                title_rect = title.get_rect(center=(WIDTH//2, 40))
                text_rect = gameoverscreen.text.get_rect(center=(WIDTH//2, HEIGHT//2))
                screen.fill((0,0,0))
                screen.blit(title,title_rect)
                screen.blit(gameoverscreen.text, text_rect)
                player.score = 0
                AI.score = 0
        #WIN SCREEN
            case 3:
                winscreen.update(selection_cursor)
                title = font.render(f"{winscreen.title}", True, (255,255,255))
                title_rect = title.get_rect(center=(WIDTH//2, 40))
                text_rect = winscreen.text.get_rect(center=(WIDTH//2, HEIGHT//2))
                screen.fill((0,0,0))
                screen.blit(title,title_rect)
                screen.blit(winscreen.text, text_rect)
                player.score = 0
                AI.score = 0

        pygame.display.flip()
        sleep(1/70)

if __name__ == "__main__":
    main()
