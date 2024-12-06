import pygame
from src.models import Player, Ghost, Wall, Pellet
from src.views import View
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, WHITE


class Controller:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pacman")
        self.clock = pygame.time.Clock()
        self.view = View(self.screen)

        self.player = Player(32, 32)

        self.ghosts = pygame.sprite.Group()
        self.ghosts.add(Ghost(128, 128))
        self.ghosts.add(Ghost(192, 128))
        self.ghosts.add(Ghost(256, 192))

        self.walls = pygame.sprite.Group()
        self.pellets = pygame.sprite.Group()

        self.build_maze()

        self.all_sprites = pygame.sprite.Group(self.player, *self.ghosts, *self.walls, *self.pellets)

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

    def show_message(self, message):
        """Display a message on the screen."""
        font = pygame.font.Font(None, 74)
        text = font.render(message, True, WHITE)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(2000)

    def run(self):
        """Run the main game loop."""
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
            self.ghosts.update(self.walls)

            if pygame.sprite.spritecollideany(self.player, self.pellets):
                pygame.sprite.spritecollide(self.player, self.pellets, True)

            if len(self.pellets) == 0:
                self.show_message("You Win!")
                running = False

            if pygame.sprite.spritecollideany(self.player, self.ghosts):
                self.show_message("Game Over!")
                running = False

            self.view.draw_sprites(self.all_sprites)
            self.view.update_display()

            self.clock.tick(FPS)

        pygame.quit()
