import pygame
from src.settings import TILE_SIZE, WHITE, YELLOW, BLUE, RED
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.direction = pygame.Vector2(0, 0)
        self.speed = 4

    def update(self, walls):
        self.rect.x += self.direction.x * self.speed
        if pygame.sprite.spritecollideany(self, walls):
            self.rect.x -= self.direction.x * self.speed

        self.rect.y += self.direction.y * self.speed
        if pygame.sprite.spritecollideany(self, walls):
            self.rect.y -= self.direction.y * self.speed

class Ghost(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 2
        self.direction = pygame.Vector2(random.choice([-1, 1]), random.choice([-1, 1]))

    def update(self, walls):
        self.rect.x += self.direction.x * self.speed
        if pygame.sprite.spritecollideany(self, walls):
            self.direction.x *= -1
            self.rect.x += self.direction.x * self.speed

        self.rect.y += self.direction.y * self.speed
        if pygame.sprite.spritecollideany(self, walls):
            self.direction.y *= -1
            self.rect.y += self.direction.y * self.speed

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(topleft=(x, y))

class Pellet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE // 2, TILE_SIZE // 2))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center=(x + TILE_SIZE // 2, y + TILE_SIZE // 2))
