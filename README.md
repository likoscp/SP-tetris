# SP-tetris

# Tetris Game 🎮

A classic Tetris game implemented in Python with PyGame. This project demonstrates clean code structure and usage of design patterns. We have created a classic Tetris game, where the player controls falling tetrominoes and clears lines to earn points. The game features the core mechanics of Tetris, a real-time scoreboard, and smooth gameplay.

## 🎮 How to Play
- **Goal**: Complete lines by correctly placing the Tetriminos. The more lines you complete, the higher your score.
- **Controls**:
  - **Left Arrow**: Move Tetrimino left
  - **Right Arrow**: Move Tetrimino right
  - **Up Arrow**: Rotate Tetrimino
  - **Down Arrow**: Speed up Tetrimino drop
  - **Enter**: Restart

## 📁 Project Structure
Here's an overview of the main files in this project:

### File Descriptions
- **main.py**: Contains the main function to initialize and start the game.
- **game.py**: Defines the Game class and includes the primary game loop for the Tetris game.
- **observer.py**: Implements the Observer and ScoreObserver classes. The ScoreObserver updates and displays the score when it changes.
- **factory.py**: Contains the TetriminoFactory class that creates new Tetrimino instances for the game.
- **view.py** Contains the View class that manages the rendering of the game board, score, game over screen, and tetrimino.
- **controller.py**:Defines the Controller class for a Tetris game, handling game logic, user input, score tracking, and rendering using pygame.
- **strategy.py**:Implements the Strategy Pattern, allowing the game to switch between different methods of player input (e.g., keyboard input). 
- **README.md**: Documentation for the project.

## Author
This project was created by Sabina, Darina, Akniyet as a practice project to learn Python game development and design patterns. 

