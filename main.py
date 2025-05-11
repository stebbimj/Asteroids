import pygame
import constants

def main():
    print("Starting Asteroids!")
    pygame.init()
    clock= pygame.time.Clock()
    dt = 0
    #print(f"Screen width: {constants.SCREEN_WIDTH}")
    #print(f"Screen height: {constants.SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    while True:    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

    # Draw a black square inside the game area and redraw it as long as the program runs
        screen.fill((0,0,0))
        pygame.display.flip()
        dt = clock.tick(60)
        dt /= 1000
        print(dt)


if __name__ == "__main__":
    main()