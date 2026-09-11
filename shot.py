import pygame
import circleshape
from constants import LINE_WIDTH, SHOT_RADIUS

class Shot(circleshape.CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen: pygame.Surface) -> None:
        print(f"drawing shot at {self.position}")
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)
