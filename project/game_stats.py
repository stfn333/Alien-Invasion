from project.settings import Settings


class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self):
        """Initialize statistics."""

        self.ai_settings = Settings()
        self.ships_left = self.ai_settings.ship_limit

        # Start game in an inactive state.
        self.game_active = False
        self.score = 0

        # High score should never be reset.
        self.high_score = 0
        self.level = 1

    def reset_stats(self):
        """Initialize statistics that can change during the game."""

        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
