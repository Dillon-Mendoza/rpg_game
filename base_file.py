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

                # Load the spritesheet using paths from settings
                self.spritesheet = SpriteSheet(self.settings.spritesheet_path, self.settings.player_config)

                # Create an instance of the character, passing settings and spritesheet
                self.character = Character(self, self.settings, self.spritesheet)

        def run_game(self):
                """Start the main loop for the game"""
                while True:
                        self._check_events()
                        keys = pygame.key.get_pressed()
                        self.character.update(keys)
                        self._update_screen()
                        self.clock.tick(60)

        def _check_events(self):
                """Respond to keypress and mouse events"""
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                sys.exit()
                        elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RIGHT:
                                        self.character.moving_right = True
                                elif  event.key == pygame.K_LEFT:
                                        self.character.moving_left = True

                        elif event.type == pygame.KEYUP:
                                if event.key == pygame.K_RIGHT:
                                        self.character.moving_right = False
                                elif event.key == pygame.K_LEFT:
                                        self.character.moving_left = False

                        elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_UP:
                                        self.character.moving_up = True
                                elif event.key == pygame.K_DOWN:
                                        self.character.moving_down = True

                        elif event.type == pygame.KEYUP:
                                if event.key == pygame.K_UP:
                                        self.character.moving_up = False
                                elif event.key == pygame.K_DOWN:
                                        self.character.moving_down = False

        def _update_screen(self):
                """Update images on the screen, and flip to the new screen"""
                self.screen.fill(self.settings.bg_color)
                self.character.blitme()

                pygame.display.flip()

if __name__ == '__main__':
        # Make a game instance, and run the game
        bf = BaseFile()
        bf.run_game()