class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initilize the game's settings"""
        # Screen settingss
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 1.5
