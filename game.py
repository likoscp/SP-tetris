import pygame
from tetris_shapes import Tetrimino

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((300, 600))
        self.clock = pygame.time.Clock()
        self.board = [[0 for _ in range(10)] for _ in range(20)]
        self.tetrimino = Tetrimino()
        self.fall_speed = 500
        self.last_move_time = pygame.time.get_ticks()
        self.score = 0  

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.move_tetrimino(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    self.move_tetrimino(1, 0)
                elif event.key == pygame.K_DOWN:
                    self.move_tetrimino(0, 1)
                elif event.key == pygame.K_UP:
                    self.rotate_tetrimino()

    def update(self):
        if pygame.time.get_ticks() - self.last_move_time > self.fall_speed:
            if not self.move_tetrimino(0, 1):
                self.merge_tetrimino()
                self.clear_full_lines()
                self.tetrimino = Tetrimino()
            self.last_move_time = pygame.time.get_ticks()

    def move_tetrimino(self, dx, dy):
        if self.check_collision(dx, dy):
            self.tetrimino.move(dx, dy)
            return True
        return False

    def rotate_tetrimino(self):
        original_shape = self.tetrimino.shape
        self.tetrimino.rotate()
        if not self.check_collision(0, 0):
            self.tetrimino.shape = original_shape

    def check_collision(self, dx, dy):
        for i, row in enumerate(self.tetrimino.shape):
            for j, block in enumerate(row):
                if block:
                    new_x = self.tetrimino.position[0] + j + dx
                    new_y = self.tetrimino.position[1] + i + dy
                    if new_x < 0 or new_x >= len(self.board[0]) or new_y >= len(self.board):
                        return False
                    if new_y >= 0 and self.board[new_y][new_x] != 0:
                        return False
        return True

    def merge_tetrimino(self):
        for i, row in enumerate(self.tetrimino.shape):
            for j, block in enumerate(row):
                if block:
                    x = self.tetrimino.position[0] + j
                    y = self.tetrimino.position[1] + i
                    self.board[y][x] = self.tetrimino.color

    def clear_full_lines(self):
        new_board = [row for row in self.board if any(block == 0 for block in row)]
        lines_cleared = len(self.board) - len(new_board)
        new_board = [[0 for _ in range(10)] for _ in range(lines_cleared)] + new_board
        self.board = new_board
        
        if lines_cleared > 0:
            self.calculate_score(lines_cleared)

    def calculate_score(self, lines_cleared):
        base_score = 10
        if lines_cleared == 1:
            self.score += base_score
        elif lines_cleared == 2:
            self.score += int(base_score * 2 * 1.2)
        elif lines_cleared == 3:
            self.score += int(base_score * 3 * 1.6)
        elif lines_cleared == 4:
            self.score += base_score * 4 * 2

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.draw_board()
        self.tetrimino.draw(self.screen)
        self.draw_score()  
        pygame.display.flip()

    def draw_board(self):
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                if self.board[y][x] != 0:
                    pygame.draw.rect(self.screen, self.board[y][x], 
                                     (x * 30, y * 30, 30, 30))

    def draw_score(self):
        font = pygame.font.Font(None, 36)
        score_surface = font.render(f'Score: {self.score}', True, (255, 255, 255))
        self.screen.blit(score_surface, (10, 10))
