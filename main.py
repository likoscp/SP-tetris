import pygame
from MVC.controller import Controller

def main():
    pygame.init()
    controller = Controller()
    controller.run()
    pygame.quit()

if __name__ == "__main__":
    main()
