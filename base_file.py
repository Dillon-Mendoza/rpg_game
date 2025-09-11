import sys
import pygame
from settings import Settings
from character import Character
from spritesheet import SpriteSheet
from button import Button

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

                self.background_music = pygame.mixer.Sound('sounds/main_menu.wav')
                # Start game in an active state                
                self.game_active = False
                # Make the Play button
                self.play_button = Button(self, "Play")
                # Make the Exit button
                self.exit_button = Button(self, "Exit")
        def run_game(self):
                """Start the main loop for the game"""
                self.background_music.play(loops=1000)
                self.background_music.set_volume(0.3)
                while True:
                        self._check_events()

                        if self.game_active:
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
                                self._check_keydown_events(event)
                        elif event.type == pygame.KEYUP:
                                self._check_keyup_events(event)
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                                mouse_pos = pygame.mouse.get_pos()
                                self._check_play_button(mouse_pos)
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                                mouse_pos = pygame.mouse.get_pos()
                                self._check_exit_button(mouse_pos)

        def _check_play_button(self, mouse_pos):
                """Start a new game when the player clicks Play"""
                if self.play_button.rect.collidepoint(mouse_pos):
                        self.game_active = True

        def _check_exit_button(self,mouse_pos):
                if self.exit_button.rect.collidepoint(mouse_pos):
                        sys.exit()


        def _check_keydown_events(self, event):
                """Respond to keypresses"""
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                                self.character.moving_right = True
                        elif  event.key == pygame.K_LEFT:
                                self.character.moving_left = True
                
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_UP:
                                        self.character.moving_up = True
                                elif event.key == pygame.K_DOWN:
                                        self.character.moving_down = True
                                elif event.key == pygame.K_ESCAPE:
                                        sys.exit()

        def _check_keyup_events(self, event):
                if event.type == pygame.KEYUP:
                        if event.key == pygame.K_RIGHT:
                                self.character.moving_right = False
                        elif event.key == pygame.K_LEFT:
                                self.character.moving_left = False

                        elif event.type == pygame.KEYUP:
                                if event.key == pygame.K_UP:
                                        self.character.moving_up = False
                                elif event.key == pygame.K_DOWN:
                                        self.character.moving_down = False


        def _update_screen(self):
                """Update images on the screen, and flip to the new screen"""
                self.screen.fill(self.settings.bg_color)
                self.character.blitme()

                # Draw the play button if the game is inactive
                if not self.game_active:
                        self.play_button.draw_button()
                        self.exit_button.draw_button()

                pygame.display.flip()

if __name__ == '__main__':
        # Make a game instance, and run the game
        bf = BaseFile()
        bf.run_game()