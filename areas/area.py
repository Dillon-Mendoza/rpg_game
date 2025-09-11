import pygame

class Area:
        """Base class for game areas"""

        def __init__(self, bf_game, bg_color=(50, 50, 100)):
                self.bf_game = bf_game
                self.screen = bf_game.screen
                self.bg_color = bg_color
                self.tiles = []
                self.npcs = []
                self.enemies = []

        def update(self):
                """Update all entities inside the area"""
                for npc in self.npsc:
                        npc.update()
                for enemy in self.enemies:
                        enemy.update()

        def draw(self):
                """Draw background, tiles, NPC's, enemies"""
                self.screen.fill(self.bg_color)

                for tile in self.tiles:
                        tile.draw(self.screen)
                for npc in self.npcs:
                        npc.blitme()
                for enemy in self.enemies:
                        enemy.blitme()