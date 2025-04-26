import pygame

from player import *

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        self.x = x
        self.y = y
        self.radius = radius
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        

    def draw(self, screen):
        # sub-classes must override
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle[a, b, c], 2)

    def update(self, dt):
        # sub-classes must override
        pass

    def collision(self, other):
        return self.position.distance_to(other.position) <= self.radius + other.radius