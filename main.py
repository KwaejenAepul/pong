import objects
import pygame
from sys import exit
from time import sleep

#game constants no touchywouchy plz uwu
WIDTH = 1800
HEIGHT = 1000
SCREEN_SIZE = WIDTH, HEIGHT

def main():
    #init some shit
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    gamestate = 0

    #initialize game objects
    font = pygame.font.SysFont('Hack', 30)
    ball = objects.pong_ball(WIDTH/2, HEIGHT/2, 20)
    player_paddle = objects.paddle(40,HEIGHT/2)

    #main loop
    while True:
        clock.tick()
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
                text = font.render(f"TITLE SCREEN {clock.get_fps()}", False, (0,0,0))
                screen.fill((240,50,126))
                screen.blit(text,(0,0))
        #GAMEPLAY
            case 1:
                fps_counter = font.render(f"{clock.get_fps()}", False, (0,0,0))
                text = font.render(f"{ball.size}", False, (0,0,0))
                ball.update(WIDTH, HEIGHT)
                player_paddle.update()
                playerrect = pygame.Rect((player_paddle.x, player_paddle.y), (player_paddle.width, player_paddle.height))
                screen.fill((240,50,126))
                screen.blit(text,(ball.x, ball.y))
                screen.blit(fps_counter, (0,0))
                pygame.draw.rect(screen, (0,0,0), playerrect )
        #GAME OVER
            case 2:
                text = font.render(f"GAME OVER {clock.get_fps()}", False, (0,0,0))
                screen.fill((240,50,126))
                screen.blit(text,(0,0))
        #WIN SCREEN
            case 3:
                text = font.render(f"WINNING {clock.get_fps()}", False, (0,0,0))
                screen.fill((240,50,126))
                screen.blit(text,(0,0))

        pygame.display.flip()
        sleep(1/70)


if __name__ == "__main__":
    main()
