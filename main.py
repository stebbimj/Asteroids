import pygame
import random
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")

    #intialize pygame, variables and group
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #adding attribute to class     
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    #calling class objects
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()
    
    while True:    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        screen.fill((0,0,0))
        
        for obj in drawable:
            obj.draw(screen)

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                return            
            for shot in shots:
                if shot.collision(asteroid):
                    if asteroid.split():
                        asteroid.kill()
                    else:
                        asteroidfield.spawn(asteroid.radius - ASTEROID_MIN_RADIUS, asteroid.position, asteroid.velocity.rotate(random.randint(20, 50)) * 1.2)
                        asteroidfield.spawn(asteroid.radius - ASTEROID_MIN_RADIUS, asteroid.position, asteroid.velocity.rotate(-random.randint(20, 50)) * 1.2)
                        asteroid.kill()
                    shot.kill()

        pygame.display.flip()

        dt = clock.tick(60)
        dt /= 1000


if __name__ == "__main__":
    main()