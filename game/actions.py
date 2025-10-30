"""
Player actions module.

Contains all the actions a player can perform during the game:
fishing, sleeping, searching for water, and exploring.
"""

import random


def fish(player):
    """
    Attempt to catch fish to restore hunger.
    
    50% chance of success. Fishing consumes energy regardless of outcome.
    
    Args:
        player (Player): The player performing the action
        
    Effects:
        - Success: +20 hunger, -10 energy
        - Failure: -15 energy
    """
    print("\n🎣 You try to fish...")
    success = random.choice([True, False])
    
    if success:
        print("✅ You caught a fish!")
        player.update_gauges(delta_hunger=20, delta_energy=-10)
    else:
        print("❌ The fish got away...")
        player.update_gauges(delta_energy=-15)


def sleep(player):
    """
    Sleep to restore energy and advance to the next day.
    
    Sleeping is essential for energy recovery but increases hunger and thirst.
    Automatically increments the days_survived counter.
    
    Args:
        player (Player): The player performing the action
        
    Effects:
        - +50 energy, -10 hunger, -10 thirst
        - Days survived +1
    """
    print("\n😴 You go to sleep...")
    player.update_gauges(delta_energy=50, delta_hunger=-10, delta_thirst=-10)
    player.days_survived += 1
    print(f"✅ You slept well! Day {player.days_survived}")


def search_water(player):
    """
    Search for fresh water to reduce thirst.
    
    50% chance of success. Searching consumes energy regardless of outcome.
    
    Args:
        player (Player): The player performing the action
        
    Effects:
        - Success: +30 thirst, -5 energy
        - Failure: -10 energy
    """
    print("\n💧 You search for water...")
    success = random.choice([True, False])
    
    if success:
        print("✅ You found fresh water!")
        player.update_gauges(delta_thirst=30, delta_energy=-5)
    else:
        print("❌ No water found...")
        player.update_gauges(delta_energy=-10)


def explore(player):
    """
    Explore the island to find resources.
    
    Random outcomes with varying effects on player stats.
    Riskier than other actions but can yield different resources.
    
    Args:
        player (Player): The player performing the action
        
    Possible outcomes:
        - Find berries: +15 hunger, -10 energy
        - Find nothing: -15 energy
        - Find water source: +20 thirst, -10 energy
        - Get lost: -20 energy
    """
    print("\n🗺️ You explore the island...")
    events = [
        ("You found some berries!", 15, 0, -10),
        ("You found nothing useful...", 0, 0, -15),
        ("You found a water source!", 0, 20, -10),
        ("You got lost and wasted energy...", 0, 0, -20),
    ]
    
    event = random.choice(events)
    message, delta_hunger, delta_thirst, delta_energy = event
    
    print(f"📢 {message}")
    player.update_gauges(delta_hunger=delta_hunger, delta_thirst=delta_thirst, delta_energy=delta_energy)
