from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_SPLIT_VELOCITY_MULTIPLIER
import random
from logger import log_event
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity
        # return asteroid

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        self.radius = self.radius - ASTEROID_MIN_RADIUS
        velocity1 = self.velocity.rotate(random_angle) * ASTEROID_SPLIT_VELOCITY_MULTIPLIER
        velocity2 = self.velocity.rotate(-random_angle) * ASTEROID_SPLIT_VELOCITY_MULTIPLIER
        asteroid1 = self.spawn(self.radius, self.position, velocity1)
        asteroid2 = self.spawn(self.radius, self.position, velocity2)
        # return [asteroid1, asteroid2]