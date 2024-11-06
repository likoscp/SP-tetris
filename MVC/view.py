
import pygame

class View:
    def __init__(self, screen):
        self.screen = screen

    def draw_board(self, board):
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] != 0:
                    pygame.draw.rect(self.screen, board[y][x], 
                                     (x * 30, y * 30, 30, 30))

    def draw_score(self, score):
        font = pygame.font.Font(None, 36)
        score_surface = font.render(f'Score: {score}', True, (255, 255, 255))
        self.screen.blit(score_surface, (10, 10))

    def draw_game_over(self):
        font = pygame.font.Font(None, 50)
        game_over_text = font.render(f'GAME OVER', True, (255, 255, 255))
        self.screen.blit(game_over_text, (50, 250))

    def draw_restart_instruction(self):
        font = pygame.font.Font(None, 30)
        restart_text = font.render(f'Press ENTER to Restart', True, (255, 255, 255))
        self.screen.blit(restart_text, (10, 40))

    def draw_tetrimino(self, tetrimino):
        tetrimino.draw(self.screen)  
