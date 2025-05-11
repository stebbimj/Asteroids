import pygame
from constants import *
from circleshape import *
from player import *

def main():
    print("Starting Asteroids!")
    pygame.init()
    clock= pygame.time.Clock()
    dt = 0
    player1 = player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    #print(f"Screen width: {constants.SCREEN_WIDTH}")
    #print(f"Screen height: {constants.SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

    # Draw a black square inside the game area and redraw it as long as the program runs
        screen.fill((0,0,0))
        player1.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60)
        dt /= 1000


if __name__ == "__main__":
    main()