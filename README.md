# Python Game Projects

Welcome to my Python Game Repository!
- **Console Python Games** – Text-based games that run in the terminal.
- **Turtle Python Games** – Graphical games built using Python's `turtle` module.

- ##  Highlighted Projects
### Console Python Games
- **[Tic Tac Toe](Console_Games/tic_tac_toe_game)** - A classic Tic-Tac-Toe game where you play against an AI. The AI uses basic strategy to win or block the player.
  - **Features:**
    - Choose your symbol (X or O).
    - AI prioritizes winning, blocking, and strategic moves.
    - Clear, numbered grid for easy input.
    - Detects wins, losses, and ties automatically.
  - **How to play:**
  1. Run `python main.py`.
  2. Choose your symbol: X or O.
  3. Enter coordinates in the format `(row,column)` to place your symbol.
  4. Play continues until a win or a tie is detected.
### Turtle Python Games
- **[Snake](Turtle_Games/snake_game)** - A classic Snake game created using Python's turtle module. The snake moves smoothly around the screen, eats food to grow longer, and the game tracks and saves your high score.
  - **Features:**
    - Smooth snake movement with segment-following behavior
    - Randomly spawning food
    - Collision detection with walls and the snake’s own body
    - Persistent high score saved in game_data.txt
  - **How to play:**
  1. Run `python main.py`.
  2. Use the arrow keys to move the snake.
  3. Eat the food to grow and increase your score.
  4. Avoid the walls and your own tail, collisions reset the snake but keep your high score.
- **[Space Invaders](Turtle_Games/space_invaders_game)** - Space-Invaders–style arcade shooter built using Python’s turtle module. Move your turtle ship, shoot enemy invaders, dodge incoming bullets, and earn points as you clear waves.
  - **Features:**
    - Player-controlled turtle ship with smooth left/right movement
    - Player bullets with collision detection
    - Enemy invaders that move as a group and change direction
    - Enemy bullets fired at random intervals
    - Scoring system with on-screen UI
    - Win condition (all enemies destroyed)
  - **How to play:**
  1. Run `python main.py`.
  2. Move left and right with the Arrow Keys.
  3. Press Space to fire bullets.
  4. Shoot all enemies to win.
  5. Avoid enemy bullets — getting hit ends the game.
