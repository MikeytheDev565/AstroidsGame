import pygame
from circleshape import CircleShape
import random
from constants import *
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        new_velocity = self.velocity.rotate(angle)
        new_velocity1 = self.velocity.rotate(-angle)
        newRadius = self.radius - ASTEROID_MIN_RADIUS
        x,y = self.position
        new_A = Asteroid(x,y, newRadius)
        new_A1 = Asteroid(x,y, newRadius)
        new_A.velocity = new_velocity * 1.2
        new_A1.velocity = new_velocity1 * 1.2