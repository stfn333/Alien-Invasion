import sys

import pygame
from pygame.sprite import Group
from project.settings import Settings
from project.ship import Ship
from project.game_stats import GameStats
from project.button import Button
from project.scoreboard import Scoreboard
import game_finctions as gf


class AlienInvasion:
    def __init__(self):
        # Initialize game and create screen object
        pygame.init()
        self.ai_settings = Settings()
        self.screen = pygame.display.set_mode((self.ai_settings.screen_width, self.ai_settings.screen_height))
        # Make a ship
        self.ship = Ship(self.screen)

        # Make a group of aliens
        self.aliens = Group()

        # Make a group to store bullets in.
        self.bullets = Group()

        # Create the fleet of aliens.
        self.fleet = gf.create_fleet(self.ai_settings, self.screen, self.ship, self.aliens)
        pygame.display.set_caption("Alien Invasion")

        # Create an instance to store game statistics.
        self.stats = GameStats()

        # Make the Play button.
        self.play_button = Button(self.screen, "Play")

        # Make a scoreboard.
        self.scoreboard = Scoreboard(self.screen, self.stats)

    def main_loop(self):
        # Start main loop for the game
        while True:
            gf.check_events(self.ai_settings, self.screen, self.stats, self.scoreboard, self.ship, self.aliens, self.bullets,
                            self.play_button)

            if self.stats.game_active:
                self.ship.update()
                gf.update_bullets(self.ai_settings, self.screen, self.stats, self.scoreboard, self.ship, self.bullets, self.aliens)
                gf.update_aliens(self.ai_settings, self.stats, self.scoreboard, self.screen, self.ship, self.aliens, self.bullets)

            gf.update_screen(self.ai_settings, self.stats, self.scoreboard, self.screen, self.ship, self.aliens,
                             self.bullets, self.play_button)


# Run game
if __name__ == "__main__":
    game = AlienInvasion()
    game.main_loop()
