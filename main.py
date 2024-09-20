import pygame
from constants import *
from player import *
from shot import *
from asteroid import *
from asteroidfield import *
import sys
def main():
    pygame.init()

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    dt = 0



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for u in updatable:
            u.update(dt)    
        
        screen.fill(color='black')

        for d in drawable:
            d.draw(screen)

        for a in asteroids:
            if player.check_collision(a):
                print("Game over!")
                sys.exit()
            for s in shots:
                if s.check_collision(a):
                    a.split()
                    s.kill()
        pygame.display.flip()

        dt = clock.tick(60) / 1000

    # print("Starting asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")
if __name__ == "__main__":
    main()