import objects
import pygame
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

    #initialize game objects
    font = pygame.font.SysFont('Hack', 30)
    ball = objects.pong_ball(WIDTH/2, HEIGHT/2, 20)
    player = objects.paddle(40,HEIGHT/2 - 75)
    AI = objects.paddle(WIDTH - 50, HEIGHT/2 - 75)

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

        match gamestate:
        #TITLESCREEN
            case 0:
                text = font.render(f"TITLE SCREEN", False, (255,255,255))
                screen.fill((0,0,0))
                screen.blit(text,(0,0))
        #GAMEPLAY
            case 1:
                player.update(HEIGHT)
                AI.AI_update(ball, HEIGHT)
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

                AIrect = pygame.Rect((AI.x, AI.y), (AI.width, AI.height))
                playerrect = pygame.Rect((player.x, player.y), (player.width, player.height))
                ballrect = pygame.Rect((ball.x, ball.y), (ball.size, ball.size))
                screen.fill((0,0,0))
                pygame.draw.rect(screen, (255,255,255), ballrect)
                pygame.draw.rect(screen, (255,255,255), playerrect)
                pygame.draw.rect(screen, (255,255,255), AIrect)
        #GAME OVER
            case 2:
                text = font.render(f"GAME OVER", False, (255,255,255))
                screen.fill((0,0,0))
                screen.blit(text,(0,0))
                player.score = 0
                AI.score = 0
        #WIN SCREEN
            case 3:
                text = font.render(f"WINNING", False, (255,255,255))
                screen.fill((0,0,0))
                screen.blit(text,(0,0))
                player.score = 0
                AI.score = 0

        pygame.display.flip()
        sleep(1/70)


if __name__ == "__main__":
    main()
