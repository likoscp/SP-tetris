# SP-tetris

# Tetris Game 🎮

A classic Tetris game implemented in Python with PyGame. This project demonstrates clean code structure and usage of design patterns.

## 📖 What is Tetris?
Tetris is a popular puzzle video game originally designed and programmed by Alexey Pajitnov in 1984. The objective is to manipulate falling blocks, known as Tetriminos, by moving and rotating them to create complete horizontal lines on the playfield. When a line is completed, it disappears, and the player earns points. The game ends when the blocks reach the top of the playfield.

## 🎮 How to Play
- **Goal**: Complete lines by correctly placing the Tetriminos. The more lines you complete, the higher your score.
- **Controls**:
  - **Left Arrow**: Move Tetrimino left
  - **Right Arrow**: Move Tetrimino right
  - **Up Arrow**: Rotate Tetrimino
  - **Down Arrow**: Speed up Tetrimino drop
  - **P**: Pause/Resume game

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
This project was created by Sabina, Darina, Danel as a practice project to learn Python game development and design patterns. 

