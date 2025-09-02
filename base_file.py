import sys
import pygame
from settings import Settings
from character import Character
from spritesheet import SpriteSheet

class BaseFile:
        """Overall class to manage game assets and behavior."""

        def __init__(self):
                """Initialize the game and create game resources."""
                pygame.init()
                self.clock = pygame.time.Clock()
                self.settings = Settings()

                self.screen = pygame.display.set_mode((
                        self.settings.screen_width, self.settings.screen_height))
                pygame.display.set_caption("Aeloria")

                # Set the background color
                self.bg_color = (30, 30, 30)

                # Load the spritesheet using paths from settings
                self.spritesheet = SpriteSheet(self.settings.spritesheet_path, self.settings.player_config)

                # Create an instance of the character, passing settings and spritesheet
                self.character = Character(self, self.settings, self.spritesheet)

        def run_game(self):
                """Start the main loop for the game"""
                while True:
                        # Watch for keyboard and mouse events.

                        # Redraw the screen during each pass through the loop
                        self.screen.fill(self.settings.bg_color)

                        # Draw the character
                        self.character.blitme()
                        
                        # Make the most recently drawn screen visible.
                        pygame.display.flip()
                        self.clock.tick(60)

        def _check_events(self):
                """Respond to keypress and mouse events"""
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                sys.exit()
                        elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RIGHT:
                                        self.character.rect.x +=1

if __name__ == '__main__':
        # Make a game instance, and run the game
        bf = BaseFile()
        bf.run_game()