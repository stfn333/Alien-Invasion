# Alien Invasion 🛸

![Alien Invasion](readme_images/capture.PNG)

## Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [How to run](#how-to-run)
- [How to Use](#how-to-use)
- [License](#license)
  
## Introduction
This is a simple shooting arcade-style video game created with Pygame. In Alien Invasion the player controls a ship that appears at the bottom center of the screen. The player can move the ship using the left and right arrow keys and shoot bullets with the space bar. When  the game begins a fleet of aliens appear moving toward the ship. The player shoots and destroys the aliens. If the player shoots all the aliens a new fleet appears that is faster than the previous one. If any alien hits the player's ship or reaches the bottom of the screen, the player loses a ship. If three ships are lost, the game ends.

## Project Structure
The project is made with the Pygame library and is organized into several classes and modules:

- **AlienInvasion:** Handles the main game loop.
- **Settings:** A class to store all settings for Alien Invasion.
- **GameStats:** Track statistics for Alien Invasion.
- **Scoreboard:** A class to report scoring information.
- **Button:** A class creating play button.
- **game_functions.py:** A module containing the main functionality of the game.
- **Ship:** Initialize a ship and set its position.
- **Bullet:** A class to manage bullets fired from the ship.
- **Alien:** A class to represent a single alien in the fleet.

## How to Run

### Prerequisites
- Python 3.12
- Pygame (for visualization)

You can install Pygame using pip:
```bash
pip install pygame
```
### Cloning the Repository
```bash
git clone https://github.com/stfn333/Alien-Invasion.git
cd Conways-Game-Of-Life
```
### Run
Once you have the repository cloned and dependencies installed, you can run the game by executing the main Python script:
```bash
python alien_invasion.py
```

## How to Use
- Click 'Play' to start or just press 'P'.
- Q: Terminate game
- Left/ Right arrow keys: Move the spaceship to the left or right.
- Space bar: Shoot bullets.
  
## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute this code as you see fit.
