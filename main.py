import pygame
from constants import *
from player import *
from asteroidfield import *
import sys
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
   
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidField = AsteroidField()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        
        for asteroid in asteroids:
            for bullet in shots:
                if bullet.check_collide(asteroid):
                    asteroid.split()
                    bullet.kill() 
                
            if player.check_collide(asteroid):
                
                sys.exit("Game over!")

        for x in drawable:
            x.draw(screen)
        
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000






if __name__ == "__main__":
    main()