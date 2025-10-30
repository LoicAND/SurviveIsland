"""
Random events module.

Manages random events that occur after each player action.
Events are weighted to control their probability of occurrence.
"""

import random


EVENTS = {
    "rain": {
        "weight": 2,
        "description": "A tropical rain falls...",
        "function": "rain"
    },
    "animal_encounter": {
        "weight": 2,
        "description": "You encounter a wild animal!",
        "function": "animal_encounter"
    },
    "fruit_found": {
        "weight": 3,
        "description": "You find some delicious fruits!",
        "function": "fruit_found"
    },
    "injury": {
        "weight": 1,
        "description": "You got injured!",
        "function": "injury"
    },
    "nothing": {
        "weight": 2,
        "description": "Nothing interesting happens...",
        "function": "nothing"
    },
    "boat_rescue": {
        "weight": 1,
        "description": "A rescue boat spots you!",
        "function": "boat_rescue"
    }
}



def rain(player):
    player.update_gauges(delta_thirst=25)
    return "🌧️ A tropical rain falls, your thirst decreases significantly."


def animal_encounter(player):
    choice = random.choice(["flee", "hunt"])
    
    if choice == "flee":
        player.update_gauges(delta_energy=-20)
        return "🐯 You encounter a wild animal and flee in panic! You lose energy."
    else:
        player.update_gauges(delta_hunger=30, delta_energy=-25)
        return "🐯 You encounter a wild animal and manage to hunt it! You gain food but lose energy."


def fruit_found(player):
    player.update_gauges(delta_hunger=20)
    return "🍎 You find some delicious fruits! Your hunger decreases."


def injury(player):
    player.update_gauges(delta_energy=-30)
    return "🩹 You got injured while exploring! You lose a lot of energy."


def nothing(player):
    return "😐 Nothing interesting happens on this day..."


def boat_rescue(player):
    return "RESCUE"


def generate_event(player):
    """
    Generate and apply a random event to the player.
    
    Events are selected based on weighted probabilities defined in EVENTS.
    The boat_rescue event returns "RESCUE" to trigger a special victory condition.
    
    Args:
        player (Player): The player affected by the event
        
    Returns:
        str: Message describing the event outcome, or "RESCUE" for boat rescue
        
    Event weights:
        - rain: 2/11 (~18%)
        - animal_encounter: 2/11 (~18%)
        - fruit_found: 3/11 (~27%)
        - injury: 1/11 (~9%)
        - nothing: 2/11 (~18%)
        - boat_rescue: 1/11 (~9%)
    """
    event_names = list(EVENTS.keys())
    weights = [EVENTS[event]["weight"] for event in event_names]
    
    chosen_event = random.choices(event_names, weights=weights, k=1)[0]
    event_info = EVENTS[chosen_event]
    
    event_function = globals()[event_info["function"]]
    message = event_function(player)
    
    return message
