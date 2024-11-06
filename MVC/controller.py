import pygame
from MVC.model import TetriminoFactory
from observer import ScoreObserver
from observer import GameObserver
from strategy import KeyboardInput
from MVC.view import View

class Controller:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Controller, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((300, 600))
        self.clock = pygame.time.Clock()
        self.board = [[0 for _ in range(10)] for _ in range(20)]
        self.tetrimino = TetriminoFactory.create_tetrimino()  
        self.fall_speed = 500
        self.level = 1
        self.last_move_time = pygame.time.get_ticks()
        self.score = 0
        self.score_observer = ScoreObserver()
        self.game_observer = GameObserver()
        self.is_game_over = False
        self.view = View(self.screen)
        self.play_background_music()
        self.input_strategy = KeyboardInput()

    def play_background_music(self):
        pygame.mixer.music.load("src/Tetris.mp3")  
        pygame.mixer.music.set_volume(0.5)  
        pygame.mixer.music.play(-1, 0.0)  

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)

    def handle_events(self):
        keys = self.input_strategy.handle_input()  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if keys[pygame.K_LEFT]:
                self.move_tetrimino(-1, 0)
            elif keys[pygame.K_RIGHT]:
                self.move_tetrimino(1, 0)
            elif keys[pygame.K_DOWN]:
                self.move_tetrimino(0, 1)
            elif keys[pygame.K_UP]:
                self.rotate_tetrimino()
            elif keys[pygame.K_SPACE]:
                self.move_tetrimino_to_bottom()
            elif keys[pygame.K_RETURN]:
                self.restart_game()

    def update(self):
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - self.last_move_time

        if elapsed_time > 10000:  
            self.last_move_time = current_time
            self.level += 6
            self.fall_speed = max(100, 500 - (self.level * 30))  

        if current_time - self.last_move_time > self.fall_speed:
            if not self.move_tetrimino(0, 1):
                self.merge_tetrimino()
                self.clear_full_lines()
                self.tetrimino = TetriminoFactory.create_tetrimino()  
            self.last_move_time = pygame.time.get_ticks()
            if any(self.board[0][x] != 0 for x in range(10)):  
                self.is_game_over = True  
                self.game_observer.update(self.is_game_over)

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

    def move_tetrimino_to_bottom(self):
        while self.check_collision(0, 1): 
            self.tetrimino.move(0, 1)  

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
        self.score_observer.update(self.score)
        

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.view.draw_board(self.board)  
        self.view.draw_tetrimino(self.tetrimino) 
        self.view.draw_score(self.score)  
        self.view.draw_restart_instruction() 
        if self.is_game_over:
            self.view.draw_game_over() 
        
            
        pygame.display.flip()

    def restart_game(self):
        self.board = [[0 for _ in range(10)] for _ in range(20)]
        self.tetrimino = TetriminoFactory.create_tetrimino()  
        self.score = 0
        self.is_game_over = False
