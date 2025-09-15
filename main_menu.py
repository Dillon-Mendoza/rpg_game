import pygame

class Menu():
        def __init__(self, base_file, settings):
                self.game = base_file
                self.settings = settings
                self.run_display = True
                self.cursor_rect = pygame.Rect(0, 0, 20, 20)
                self.offset = -100

        def draw_cursor(self):
                self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

        def blitme(self):
                self.game.window.blit(self.game.display, (0, 0))
                pygame.display.update()
                self.game.reset_keys()

class MainMenu(Menu):
        def __init__(self, game):
                Menu.__init__(self, game, game.settings)
                self.state = "Start"
                self.startx, self.starty = self.settings.screen_width // 2, self.settings.screen_height // 2
                self.creditsx, self.creditsy = self.settings.screen_height, self.settings.screen_width + 50 #Option
                self.exitx, self.exity = self.settings.screen_height, self.settings.screen_width + 70 #Credits
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

        def display_menu(self):
                self.run_display = True
                while self.run_display:
                        self.game._check_events()
                        self.check_input()
                        self.game.screen.fill((0, 0, 0))
                        self.game.draw_text("Aeloria", 20, self.game.settings.screen_width, self.game.settings.screen_height /2 - 20)
                        self.game.draw_text('Start Game', 20, self.startx, self.starty)
                        self.game.draw_text('Credits', 20, self.creditsx, self.creditsy)
                        self.game.draw_text('Exit', 20, self.exitx, self.exity)
                        self.draw_cursor()
                        self.blit_screen()

        def move_cursor(self):
                if self.game.DOWN_KEY:
                        if self.state == 'Start':
                                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                                self.state = 'Credits'
                        elif self.state == 'Credits':
                                self.cursor_rect.midtop = (self.exitx + self.offset, self.exity)
                                self.state = 'Exit'
                        elif self.state == 'Exit':
                                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                                self.state = 'Start'
                if self.game.UP_KEY:
                        if self.state == 'Start':
                                self.cursor_rect.midtop = (self.exitx + self.offset, self.exity)
                                self.state = 'Exit'
                        elif self.state == 'Credits':
                                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                                self.state = 'Start'
                        elif self.state == 'Exit':
                                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                                self.state = 'Credits'

        def check_input(self):
                self.move_cursor()
                if self.game.START_KEY:
                        if self.state == 'Start':
                                self.game.playing = True
                        elif self.state == 'Credits':
                                pass
                        elif self.state == 'Exit':
                                pass
                        self.run_display = False