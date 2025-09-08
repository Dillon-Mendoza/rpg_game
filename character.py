import pygame
from settings import Settings


class Character(pygame.sprite.Sprite):
    """A class to manage the character with animations."""

    def __init__(self, bf_game, settings, spritesheet=None):
        """Initialize the character and set its starting position."""
        super().__init__()
        self.screen = bf_game.screen
        self.screen_rect = bf_game.screen.get_rect()
        self.settings = bf_game.settings
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # Load animations from spritesheet if provided
        if spritesheet:
            self.animations = {
                "idle": spritesheet.get_animations("idle"),
                "walk": spritesheet.get_animations("walk"),
            }
        else:
            self.animations = {"idle": [], "walk": []}

        # Animation state
        self.current_animation = "idle"
        self.frame_index = 0
        if self.animations["idle"]:
            self.image = self.animations[self.current_animation][self.frame_index]
            self.rect = self.image.get_rect(center=self.screen_rect.center)
        else:
            self.image = pygame.Surface((32, 32))  # Default placeholder
            self.image.fill((255, 0, 255))  # Magenta for visibility
            self.rect = self.screen_rect.copy()
            self.x = float(self.rect.x)

        # Movement settings
        self.speed = self.settings.player_speed
        self.animation_speed = self.settings.player_animation_speed

    def update(self, keys):
        """Update character position and animation."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.speed
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.speed

        # Set animation state
        #self.current_animation = "walk" if self.moving else "idle"

        # Cycle through frames only if frames exist
        frames = self.animations.get(self.current_animation, [])
        if frames:
            self.frame_index += self.animation_speed
            if self.frame_index >= len(frames):
                self.frame_index = 0
            self.image = frames[int(self.frame_index)]
        # else: keep current image (placeholder)

    def blitme(self):
        """Draw the character at its current location."""
        self.screen.blit(self.image, self.rect)
