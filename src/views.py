import pygame
from src.settings import BLACK

class View:
    def __init__(self, screen):
        self.screen = screen

    def draw_sprites(self, sprites):
        self.screen.fill(BLACK)
        sprites.draw(self.screen)

    def update_display(self):
        pygame.display.flip()
