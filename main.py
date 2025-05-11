import pygame
from constants import *
from player import Player
#from circleshape import CircleShape

def main():
    print("Starting Asteroids!")

    #intialize pygame, variables and group
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    #adding attribute to class     
    Player.containers = (updatable, drawable)

    #calling class objects
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    
    while True:    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        screen.fill((0,0,0))
        
        for obj in drawable:
            obj.draw(screen)
            

        pygame.display.flip()

        dt = clock.tick(60)
        dt /= 1000


if __name__ == "__main__":
    main()