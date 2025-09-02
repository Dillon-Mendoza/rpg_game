class Settings:
        """A class to store all settings for Aeloria game."""
        def __init__(self):
                """Initialize the game's settings."""
                # Screen settings
                self.screen_width = 1000
                self.screen_height = 600
                self.bg_color = (30, 30, 30)

                # Player settings
                self.player_start_x = 400
                self.player_start_y = 300
                self.player_speed = 2.0
                self.player_animation_speed = 0.15

                # File paths
                self.spritesheet_path = 'images/16x16 Idle-Sheet.png'
                self.player_config = 'player.json'