# 🏝️ SurviveIsland

## Project Overview

SurviveIsland is a text-based survival game developed in Python. You play as a castaway on a desert island and must manage your resources (hunger, thirst, energy) to survive as long as possible.

The game features:
- Survivor customization (name and survival goal)
- 4 different actions (fish, sleep, search for water, explore)
- Random events that influence your survival
- Automatic save system
- Two possible endings: complete survival or boat rescue

## Game Rules

### Objective
Survive the number of days you chose (between 10 and 50 days) by keeping your vital statistics above 0.

### Vital Statistics
- **Hunger**: Decreases over time. Reach 0 = Game Over
- **Thirst**: Decreases over time. Reach 0 = Game Over
- **Energy**: Required to perform actions. Reach 0 = Game Over

### Available Actions
1. **Fish** 🎣: 50% chance to catch a fish (+20 hunger, -10 energy)
2. **Sleep** 😴: Restores energy (+50 energy, -10 hunger, -10 thirst) and advances one day
3. **Search for water** 💧: 50% chance to find water (+30 thirst, -5 energy)
4. **Explore** 🗺️: Random event with different rewards or penalties
5. **Quit and save** 💾: Save your progress

### Random Events
After each action, a random event can occur:
- 🌧️ **Tropical rain**: +25 thirst
- 🐯 **Animal encounter**: Flee (-20 energy) or successful hunt (+30 hunger, -25 energy)
- 🍎 **Fruits found**: +20 hunger
- 🩹 **Injury**: -30 energy
- 😐 **Nothing**: No effect
- 🚢 **Rescue boat**: Instant victory!

### Victory Conditions
- Survive the number of days chosen at the start of the game
- Be spotted by a rescue boat (random event)

### Defeat Conditions
- One of your vital statistics (hunger, thirst, or energy) reaches 0

## How to Run the Program

### Prerequisites
- Python 3.x installed on your machine

### Installation and Launch

1. **Clone the repository**:
```bash
git clone https://github.com/LoicAND/SurviveIsland.git
cd SurviveIsland
```

2. **Run the game**:
```bash
python main.py
```

3. **Play**:
   - Choose whether to load a saved game (y/n)
   - Enter your name
   - Set your survival goal (10-50 days)
   - Follow on-screen instructions and choose your actions (1-5)

### Project Structure
```
SurviveIsland/
├── main.py              # Game entry point
├── game/
│   ├── player.py        # Player management
│   ├── actions.py       # Available actions
│   ├── evenements.py    # Random events
│   ├── gestion.py       # Main game loop
│   └── save.py          # Save system
├── data/
│   └── save.json        # Save file (auto-generated)
└── README.md
```

---

**Good luck, survivor!** 🏝️🌴
