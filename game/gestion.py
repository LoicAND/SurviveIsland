from game.player import Player
from game.actions import fish, sleep, search_water, explore
from game.evenements import generate_event
from game.save import save_game, load_game, delete_save


def display_gauges(player):
    print(f"\n📅 Day {player.days_survived} - 🏝️ {player.name.upper()}")
    print("=" * 40)
    print(f"Hunger: {player.hunger}/100 | Thirst: {player.thirst}/100 | Energy: {player.energy}/100")
    print("=" * 40)


def choose_action():
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
    print("\n" + "="*50)
    print("🏝️  WELCOME TO SURVIVE ISLAND  🏝️")
    print("="*50)
    print("\nYour goal: Survive 10 days on a desert island!")
    print("Manage your hunger, thirst, and energy wisely.")
    print("="*50 + "\n")
    
    load_choice = input("📂 Do you want to load a saved game? (y/n): ").strip().lower()
    
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
    
    total_days = 10
    
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
        print(event_message)
        
        player.update_gauges(delta_hunger=-5, delta_thirst=-5, delta_energy=-3)
        
        if action_choice != "2":
            player.days_survived += 1
        
        save_game(player, player.days_survived)
    
    replay = input("\n🔄 Do you want to play again? (y/n): ").strip().lower()
    if replay == "y":
        game_loop()
    else:
        print("\n👋 Thanks for playing! See you next time!")


if __name__ == "__main__":
    game_loop()
