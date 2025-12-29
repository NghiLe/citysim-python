# CitySim – City Simulation Game (Python)

CitySim is a console based city simulation game written in Python.  
Players manage a small city by making decisions through numeric inputs, which directly affect population, revenue, infrastructure, and overall city growth.

The game runs as a turn-based simulation where each action and random event can influence the long-term state of the city.


## What the game does
- Displays a city map using text and ANSI color codes
- Allows the player to build structures such as houses, streets, and rivers
- Tracks city statistics including population and revenue
- Simulates random natural disasters (e.g., earthquakes, volcanoes)
- Updates the city state after each turn based on player actions and events


## How the game works
- The player interacts with the game by entering numeric choices from a menu
- Each turn represents a simulation step
- Player decisions and random events modify the city map and statistics
- The simulation continues until the player chooses to exit or the city can no longer sustain itself


## What I learned
- Using Python functions (`def`) to organize game logic
- Managing game state across multiple turns
- Working with loops and conditional logic in a simulation
- Using 2D arrays to represent a grid-based map
- Applying ANSI escape codes to render colored output in the console
- Handling randomness to simulate unpredictable events

---

## How to run the game
Make sure Python is installed, then run:

```bash
python CitySim_project2.py
```
