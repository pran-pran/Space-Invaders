# Space Invaders Game

## Overview

Space Invaders is a classic arcade game where you control a spaceship to shoot down invading aliens. This project, developed using Python and Pygame, brings the nostalgic arcade experience to modern screens with enhanced visuals, sound effects, and levels.

## Features

- **Classic Gameplay:** Defend Earth from alien invaders with your spaceship.
- **Dynamic Levels:** Increase difficulty as you progress through levels.
- **Sound Effects:** Enjoy background music and sound effects for a more immersive experience.
- **Score Tracking:** Keep track of your high scores and compete with friends.

## Installation

To run the Space Invaders game on your local machine, follow these steps:

### Prerequisites

- Python 3.x
- Pygame library

### Installation Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/pran-pran//space-invaders.git

2.**Navigate to the Project Directory:**
   cd Space-Invaders
   
3. **Install Dependencies:**
  Make sure you have Python and Pygame installed. You can install Pygame using pip:
  pip install pygame

 4. **Run the Game:**
     space_invaders.py

## Challenges and Resolutions

1. **Collision Detection:**
   - **Issue:** Accurate detection of when bullets hit enemies.
   - **Approach:** Implemented a distance-based collision detection system. By calculating the distance between bullets and enemies, the game can determine collisions accurately.

2. **Enemy Movement:**
   - **Issue:** Ensuring smooth movement and proper boundary handling for enemies.
   - **Approach:** Developed horizontal movement mechanics with boundary checks. Enemies move back and forth within the screen limits, reversing direction when hitting the edges for fluid gameplay.

3. **Game Over Management:**
   - **Issue:** Handling game over scenarios and providing a restart option.
   - **Approach:** Created a game over screen that appears when the game ends. Included functionality to restart the game by waiting for the player to press the SPACE bar.

## Lessons Learned

- **Game Development Insights:** Gained practical experience in game mechanics and the use of Pygame for game creation.
- **Enhanced Problem-Solving Skills:** Improved ability to troubleshoot and solve issues related to game logic, collision detection, and user interaction.

## Links
https://youtu.be/FfWpgLFMI7w?si=VQ9Mx-mdCJJH2J2W - This video guided the development of the game.
https://github.com/pran-pran/Space-Invaders.git - GitHub Repository

