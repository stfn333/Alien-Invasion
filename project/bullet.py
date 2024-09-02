import pygame

from pygame.sprite import Sprite
from project.settings import Settings


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, screen, ship):
        """Create a bullet object at the ship's current position."""

        super().__init__()
        self.screen = screen
        self.ai_settings = Settings()
        self.ship = ship

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.ai_settings.bullet_width, self.ai_settings.bullet_height)
        self.rect.centerx = self.ship.rect.centerx
        self.rect.bottom = self.ship.rect.top

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

        self.color = self.ai_settings.bullet_color
        self.speed_factor = self.ai_settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen."""

        # Update the decimal position of the bullet.
        self.y -= self.speed_factor

        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""

        pygame.draw.rect(self.screen, self.color, self.rect)
