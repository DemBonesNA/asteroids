import pygame
import sys
from constants import *
from player import *
from asteroidfield import *
from circleshape import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    shot = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroid, updatable, drawable)
    Shot.containers = (shot, updatable, drawable)
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
        for item in asteroid:
            if item.collision(player):
                print("Game over!")
                sys.exit()
            for bullets in shot:
                if item.collision(bullets):
                    pygame.sprite.Sprite.kill(bullets)
                    item.split()
        pygame.Surface.fill(screen, (0,0,0))
        for things in drawable:
            things.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000

    print(f"""
    Starting Asteroids! 
    Screen width: {SCREEN_WIDTH} 
    Screen height: {SCREEN_HEIGHT}
    """)

if __name__ == "__main__":
    main()    