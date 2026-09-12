import random

import pygame
import circleshape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE_SECONDS, ASTEROID_MAX_RADIUS, LINE_WIDTH
from logger import log_event

# Base class for asteroid objects
class Asteroid(circleshape.CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        print(f"drawing asteroid at {self.position}")
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

    def split(self) -> None:
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            log_event("asteroid_split")
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_angle_1 = random.uniform(20,50)
            new_angle_2 = - new_angle_1
            new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_1.velocity = self.velocity.rotate(new_angle_1)
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_2.velocity = self.velocity.rotate(new_angle_2)
