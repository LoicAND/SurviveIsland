import random


def fish(player):
    print("\n🎣 You try to fish...")
    success = random.choice([True, False])
    
    if success:
        print("✅ You caught a fish!")
        player.update_gauges(delta_hunger=20, delta_energy=-10)
    else:
        print("❌ The fish got away...")
        player.update_gauges(delta_energy=-15)


def sleep(player):
    print("\n😴 You go to sleep...")
    player.update_gauges(delta_energy=50, delta_hunger=-10, delta_thirst=-10)
    player.days_survived += 1
    print(f"✅ You slept well! Day {player.days_survived}")


def search_water(player):
    print("\n💧 You search for water...")
    success = random.choice([True, False])
    
    if success:
        print("✅ You found fresh water!")
        player.update_gauges(delta_thirst=30, delta_energy=-5)
    else:
        print("❌ No water found...")
        player.update_gauges(delta_energy=-10)


def explore(player):
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
