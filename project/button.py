import pygame

from project.settings import Settings


class Button:
    def __init__(self, screen, msg):
        """Initialize button attributes."""

        self.ai_settings = Settings()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width = self.ai_settings.button_width
        self.height = self.ai_settings.button_height
        self.button_color = self.ai_settings.button_color
        self.text_color = self.ai_settings.button_text_color
        self.font = self.ai_settings.button_font

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once.
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
