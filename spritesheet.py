import pygame
import json

class SpriteSheet:
        def __init__(self, image_path, config_file):
                """Load a sprite sheet and config file (JSON)."""
                self.sheet = pygame.image.load(image_path).convert_alpha()
                with open(config_file) as f:
                        self.config = json.load(f)

                self.frame_width = self.config['frame_width']
                self.frame_height = self.config['frame_height']
                self.animations = self.config['animations']

                # Slice all frames into a list
                self.frames = self._slice_sheet()

        def _slice_sheet(self):
                """Cut the sprite sheet into individual frames."""
                frames = []
                sheet_width, sheet_height = self.sheet.get_size()
                for y in range(0, sheet_height, self.frame_height):
                        for x in range(0, sheet_width, self.frame_width):
                                rect = pygame.Rect(x, y, self.frame_width, self.frame_height)
                                frame = self.sheet.subsurface(rect).copy()
                                frames.append(frame)
                return frames
        
        def get_animations(self, name):
                """Return a list of frames for a given animation name"""
                return [self.frames[i] for i in self.animations[name]]