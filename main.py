import pygame
from src.controller import Controller  # Import the controller

def main():
    pygame.init()
    game = Controller()  # Create an instance of the Controller object
    game.run()  # Call the mainloop

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
