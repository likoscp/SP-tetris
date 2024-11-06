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
- **tetrimino.py**: Contains the `Tetrimino` class with configurations for different shapes and colors.
- **input_strategy.py**: Defines `InputStrategy` and `KeyboardInput` classes, allowing flexible input handling.
- **observer.py**: Implements `Observer` and `ScoreObserver` classes to update and display the score.
- **factory.py**: Contains the `TetriminoFactory` class for creating Tetrimino instances.
- **README.md**: Documentation for the project.
- **requirements.txt**: Lists required Python packages, mainly PyGame.

## Author
This project was created by Sabina, Darina, Akniyet as a practice project to learn Python game development and design patterns. 

