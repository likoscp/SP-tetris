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
- **game.py**: Defines the `Game` class and includes the primary game loop.
- **observer.py**: Implements `Observer` and `ScoreObserver` classes to update and display the score.
- **factory.py**: Contains the `TetriminoFactory` class for creating Tetrimino instances.
- **controller.py**:Defines the Controller class for a Tetris game, handling game logic, user input, score tracking, and rendering using pygame.
- **strategy.py**:The Strategy Pattern is used to handle different methods of player input, allowing the game to easily switch between various input strategies 
- **README.md**: Documentation for the project.

## Author
This project was created by Sabina, Darina, Akniyet as a practice project to learn Python game development and design patterns. 

