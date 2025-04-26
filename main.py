import pygame
import sys
from constants import *
from player import *
from asteroidfield import *
from circleshape import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    circleshape = CircleShape(ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS, PLAYER_RADIUS)
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for item in asteroids:
            if item.collision(player):
                print("Game over!")
                sys.exit()
        pygame.Surface.fill(screen, (0,0,0))
        for items in drawable:
            items.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000

    print(f"""
    Starting Asteroids! 
    Screen width: {SCREEN_WIDTH} 
    Screen height: {SCREEN_HEIGHT}
    """)

if __name__ == "__main__":
    main()    