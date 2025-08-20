import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        rand_angle = random.uniform(20,50)
        nu_vec1 = self.velocity.rotate(rand_angle)
        nu_vec2 = self.velocity.rotate(-rand_angle)

        nu_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x,self.position.y,nu_radius)
        asteroid1.velocity = nu_vec1 * 1.2

        asteroid2 = Asteroid(self.position.x, self.position.y,nu_radius)
        asteroid2.velocity = nu_vec2 * 1.2


