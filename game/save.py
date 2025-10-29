import json
import os
from game.player import Player


SAVE_FILE = "data/save.json"


def save_game(player, current_day):
    save_data = {
        "day": current_day,
        "player": {
            "name": player.name,
            "hunger": player.hunger,
            "thirst": player.thirst,
            "energy": player.energy,
            "days_survived": player.days_survived
        }
    }
    
    os.makedirs(os.path.dirname(SAVE_FILE), exist_ok=True)
    
    try:
        with open(SAVE_FILE, 'w') as f:
            json.dump(save_data, f, indent=2)
        print("\n💾 Game saved successfully!")
        return True
    except Exception as e:
        print(f"\n❌ Error saving game: {e}")
        return False


def load_game():
    if not os.path.exists(SAVE_FILE):
        print("\n📂 No save file found. Starting a new game...")
        return None, None
    
    try:
        with open(SAVE_FILE, 'r') as f:
            content = f.read().strip()
            if not content:
                print("\n📂 Save file is empty. Starting a new game...")
                return None, None
            
            save_data = json.loads(content)
        
        player_data = save_data.get("player", {})
        current_day = save_data.get("day", 0)
        
        player = Player(
            name=player_data.get("name", "Survivor"),
            hunger=player_data.get("hunger", 100),
            thirst=player_data.get("thirst", 100),
            energy=player_data.get("energy", 100),
            days_survived=player_data.get("days_survived", 0)
        )
        
        print(f"\n✅ Game loaded! Welcome back, {player.name}!")
        print(f"Resuming from day {current_day}...")
        return player, current_day
    
    except json.JSONDecodeError:
        print("\n⚠️ Save file is corrupted. Starting a new game...")
        return None, None
    except Exception as e:
        print(f"\n❌ Error loading game: {e}. Starting a new game...")
        return None, None


def delete_save():
    if os.path.exists(SAVE_FILE):
        try:
            os.remove(SAVE_FILE)
            print("\n🗑️ Save file deleted.")
            return True
        except Exception as e:
            print(f"\n❌ Error deleting save file: {e}")
            return False
    return True
