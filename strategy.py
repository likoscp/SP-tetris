import pygame
class InputStrategy:
    def handle_input(self):
        raise NotImplementedError()

class KeyboardInput(InputStrategy):
    def handle_input(self):
        keys = pygame.key.get_pressed()
