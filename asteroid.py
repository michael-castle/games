import random

import pygame

from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.position, self.radius, width=2)
        
    def update(self, dt):
        self.position += self.velocity*dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        asteroid1 = Asteroid(self.position[0], self.position[1], self.radius-ASTEROID_MIN_RADIUS)
        asteroid2 = Asteroid(self.position[0], self.position[1], self.radius-ASTEROID_MIN_RADIUS)
        asteroid1.velocity = self.velocity.rotate(angle)*1.2
        asteroid2.velocity = self.velocity.rotate(-angle)*1.2