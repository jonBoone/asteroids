import pygame
import circleshape
from shot import Shot
from constants import LINE_WIDTH, PLAYER_RADIUS, PLAYER_SHOOT_COOLDOWN_SECONDS, PLAYER_SHOOT_SPEED, PLAYER_SPEED, PLAYER_TURN_SPEED


# Base class for player objects
class Player(circleshape.CircleShape):
    def __init__(self, x: float, y: float) -> None:

        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0.0
        self.shoot_cooldown_seconds = 0.0

    # in the Player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt: float) -> None:

        self.shoot_cooldown_seconds -= dt
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt: float) -> None:
        unit_vector = pygame.Vector2(0,1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self) -> None:
        if self.shoot_cooldown_seconds > 0:
            return  # Still in cooldown, cannot shoot yet
        
        self.shoot_cooldown_seconds = PLAYER_SHOOT_COOLDOWN_SECONDS  # Reset cooldown
        # Create a new shot object at the player's position
        shot = Shot(self.position.x, self.position.y)
        # Set the shot's velocity based on the player's rotation
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        # Add the shot to the appropriate sprite groups
        self.containers[0].add(shot)  # updatable group
        self.containers[1].add(shot)  # drawable group