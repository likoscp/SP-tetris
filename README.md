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
### MVC Architecture
- **controller.py**:Defines the Controller class, which acts as the intermediary between the model and the view. It handles game logic, user input, score tracking, and rendering using pygame.
- **model.py**:Contains the game's core logic, including the TetriminoFactory and the Game class for managing the game state, tetrimino creation, board handling, and line clearing.
- **view.py** : Manages the rendering of the game, including the game board, tetriminoes, score, game over screen, and restart instructions.

### Additional Files
- **main.py**: Contains the main function to initialize and start the game.
- **observer.py**: Implements the Observer and ScoreObserver classes. The ScoreObserver listens for score changes and updates the score display.
- **factory.py**: Contains the TetriminoFactory class that creates new Tetrimino instances for the game.
- **strategy.py**:Implements the Strategy Pattern to handle different methods of player input. The KeyboardInput class is used to read player input from the keyboard.
- **README.md**: Documentation for the project.

## Author
This project was created by Sabina, Darina, Akniyet as a practice project to learn Python game development and design patterns. 

