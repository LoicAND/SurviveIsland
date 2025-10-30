"""
Game management module.

Contains the main game loop and all game flow control functions.
Manages player actions, event triggers, victory/defeat conditions, and UI display.
"""

from game.player import Player
from game.actions import fish, sleep, search_water, explore
from game.evenements import generate_event
from game.save import save_game, load_game, delete_save


def display_gauges(player):
    """
    Display the player's current statistics in a formatted way.
    
    Shows day counter, player name, and all vital stats (hunger, thirst, energy).
    
    Args:
        player (Player): The player whose stats to display
    """
    print(f"\n📅 Day {player.days_survived} - 🏝️ {player.name.upper()}")
    print("=" * 40)
    print(f"Hunger: {player.hunger}/100 | Thirst: {player.thirst}/100 | Energy: {player.energy}/100")
    print("=" * 40)


def choose_action():
    """
    Display action menu and get player's choice.
    
    Validates input to ensure a valid action is selected.
    
    Returns:
        str: The chosen action number (1-5) as a string
        
    Actions:
        1 - Fish
        2 - Sleep
        3 - Search for water
        4 - Explore
        5 - Quit and save
    """
    print("\n🎮 What do you want to do?")
    print("1 - Fish 🎣")
    print("2 - Sleep 😴")
    print("3 - Search for water 💧")
    print("4 - Explore 🗺️")
    print("5 - Quit and save 💾")
    
    while True:
        try:
            choice = input("\nYour choice (1-5): ").strip()
            if choice in ["1", "2", "3", "4", "5"]:
                return choice
            else:
                print("❌ Invalid choice. Please enter 1, 2, 3, 4, or 5.")
        except:
            print("❌ Invalid input. Please try again.")


def check_conditions(player, current_day, total_days):
    """
    Check if the game should end (victory or defeat).
    
    Args:
        player (Player): The player to check
        current_day (int): Current day in the game
        total_days (int): Target number of days to survive
        
    Returns:
        tuple: (continue_game, message)
            - continue_game (bool): True if game should continue, False if ended
            - message (str): Victory or defeat message if game ended, empty string otherwise
            
    End conditions:
        - Defeat: Any vital stat (hunger, thirst, energy) reaches 0
        - Victory: Survived the target number of days
    """
    if not player.is_alive():
        cause = []
        if player.hunger <= 0:
            cause.append("hunger")
        if player.thirst <= 0:
            cause.append("thirst")
        if player.energy <= 0:
            cause.append("energy")
        
        return False, f"💀 GAME OVER! You died from {' and '.join(cause)}..."
    
    if current_day >= total_days:
        return False, f"🎉 VICTORY! You survived {total_days} days on the island! Well done!"
    
    return True, ""


def game_loop():
    """
    Main game loop - the heart of the game.
    
    Manages the entire game flow:
    1. Welcome screen and game setup
    2. Load existing save or create new player
    3. Player name input
    4. Custom survival days goal (10-50)
    5. Main turn-based loop:
       - Display stats
       - Check win/lose conditions
       - Get player action
       - Apply action effects
       - Generate random event
       - Handle boat rescue (alternative victory)
       - Auto-save progress
    6. Game over handling and replay option
    
    Special features:
    - Auto-save after each turn
    - Quit and save option (action 5)
    - Boat rescue random event for alternative victory
    - Custom survival goal between 10-50 days
    """
    print("\n" + "="*50)
    print("🏝️  WELCOME TO SURVIVE ISLAND  🏝️")
    print("="*50)
    
    load_choice = input("\n📂 Do you want to load a saved game? (y/n): ").strip().lower()
    
    if load_choice == "y":
        player, current_day = load_game()
        if player is None:
            player_name = input("\n👤 Enter your name: ").strip() or "Survivor"
            player = Player(name=player_name)
            print(f"\n🌴 Welcome, {player.name}! Good luck!\n")
    else:
        player_name = input("\n👤 Enter your name: ").strip() or "Survivor"
        player = Player(name=player_name)
        print(f"\n🌴 Welcome, {player.name}! Good luck!\n")
    
    while True:
        try:
            days_input = input("🎯 How many days do you think you can survive? (10-50): ").strip()
            total_days = int(days_input)
            if 10 <= total_days <= 50:
                break
            else:
                print("❌ Please enter a number between 10 and 50.")
        except ValueError:
            print("❌ Please enter a valid number.")
    
    print(f"\n🏝️ Your goal: Survive {total_days} days on a desert island!")
    print("Manage your hunger, thirst, and energy wisely.")
    print("="*50 + "\n")
    
    while True:
        display_gauges(player)
        
        continue_game, message = check_conditions(player, player.days_survived, total_days)
        
        if not continue_game:
            print("\n" + "="*50)
            print(message)
            print("="*50 + "\n")
            delete_save()
            break
        
        action_choice = choose_action()
        
        if action_choice == "5":
            save_game(player, player.days_survived)
            print("\n👋 Game saved! See you next time!")
            return
        
        print("\n" + "-"*40)
        if action_choice == "1":
            fish(player)
        elif action_choice == "2":
            sleep(player)
        elif action_choice == "3":
            search_water(player)
        elif action_choice == "4":
            explore(player)
        
        print("-"*40)
        
        print("\n🎲 Random event...")
        event_message = generate_event(player)
        
        if event_message == "RESCUE":
            print("🚢 A RESCUE BOAT SPOTTED YOU!")
            print("They're coming to save you!")
            print("\n" + "="*50)
            print(f"🎉 RESCUED! You survived {player.days_survived} days and got rescued!")
            print("="*50 + "\n")
            delete_save()
            break
        
        print(event_message)
        
        player.update_gauges(delta_hunger=-5, delta_thirst=-5, delta_energy=-3)
        
        # Each action = 1 day
        player.days_survived += 1
        
        save_game(player, player.days_survived)
    
    replay = input("\n🔄 Do you want to play again? (y/n): ").strip().lower()
    if replay == "y":
        game_loop()
    else:
        print("\n👋 Thanks for playing! See you next time!")


if __name__ == "__main__":
    game_loop()
