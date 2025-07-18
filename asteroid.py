import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, r):
        super().__init__(x, y, r)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity
