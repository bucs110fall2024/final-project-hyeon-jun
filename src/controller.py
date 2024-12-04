import pygame
from src.models import Player, Ghost, Wall, Pellet
from src.views import View
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS

class Controller:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pacman")
        self.clock = pygame.time.Clock()
        self.view = View(self.screen)

        self.player = Player(32, 32)
        self.ghost = Ghost(128, 128)
        self.walls = pygame.sprite.Group()
        self.pellets = pygame.sprite.Group()

        self.build_maze()

        self.all_sprites = pygame.sprite.Group(self.player, self.ghost, *self.walls, *self.pellets)

    def build_maze(self):
        maze = [
            "WWWWWWWWWWWWWWWWWW",
            "W................W",
            "W.WWW.WWWW.WWWW.WW",
            "W.W.............W",
            "W.WWW.WW.WW.WWW.W",
            "W................W",
            "WWWWWWWWWWWWWWWWWW"
        ]

        for row_index, row in enumerate(maze):
            for col_index, col in enumerate(row):
                x = col_index * 32
                y = row_index * 32
                if col == "W":
                    wall = Wall(x, y)
                    self.walls.add(wall)
                elif col == ".":
                    pellet = Pellet(x, y)
                    self.pellets.add(pellet)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.player.direction = pygame.Vector2(-1, 0)
            elif keys[pygame.K_RIGHT]:
                self.player.direction = pygame.Vector2(1, 0)
            elif keys[pygame.K_UP]:
                self.player.direction = pygame.Vector2(0, -1)
            elif keys[pygame.K_DOWN]:
                self.player.direction = pygame.Vector2(0, 1)
            else:
                self.player.direction = pygame.Vector2(0, 0)

            self.player.update(self.walls)
            self.ghost.update(self.walls)

            if pygame.sprite.spritecollideany(self.player, self.pellets):
                pygame.sprite.spritecollide(self.player, self.pellets, True)

            if pygame.sprite.collide_rect(self.player, self.ghost):
                print("Game Over!")
                running = False

            self.view.draw_sprites(self.all_sprites)
            self.view.update_display()

            self.clock.tick(FPS)

        pygame.quit()
