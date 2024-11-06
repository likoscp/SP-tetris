import random
import pygame

class Tetrimino:
    SHAPES = [
        {'shape': [[1, 1, 1, 1]], 'color': (0, 255, 255)},  
        {'shape': [[1, 1, 1], [0, 1, 0]], 'color': (128, 0, 128)},  
        {'shape': [[1, 1], [1, 1]], 'color': (255, 255, 0)}, 
        {'shape': [[0, 1, 1], [1, 1, 0]], 'color': (0, 255, 0)},  
        {'shape': [[1, 1, 0], [0, 1, 1]], 'color': (255, 0, 0)}, 
        {'shape': [[1, 1, 1], [1, 0, 0]], 'color': (255, 165, 0)},  
        {'shape': [[1, 1, 1], [0, 0, 1]], 'color': (0, 0, 255)},  
    ]

    def __init__(self):
        chosen_shape = random.choice(Tetrimino.SHAPES)
        self.shape = chosen_shape['shape']
        self.color = chosen_shape['color']
        self.position = [4, 0]

    def move(self, dx, dy):
        self.position[0] += dx
        self.position[1] += dy

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

    def draw(self, surface):
        for i, row in enumerate(self.shape):
            for j, block in enumerate(row):
                if block:
                    pygame.draw.rect(surface, self.color, 
                                     (self.position[0] * 30 + j * 30, 
                                      self.position[1] * 30 + i * 30, 30, 30))
