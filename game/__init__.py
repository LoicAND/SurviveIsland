"""
SurviveIsland game package.

This package contains all the game modules:
- player: Player class and statistics management
- actions: Available player actions (fish, sleep, search_water, explore)
- evenements: Random events system
- gestion: Main game loop and flow control
- save: Save/load game system
"""

from game.player import Player
from game.actions import fish, sleep, search_water, explore
from game.evenements import generate_event
from game.save import save_game, load_game, delete_save
from game.gestion import game_loop, display_gauges, choose_action, check_conditions

__all__ = [
    # Player
    'Player',
    # Actions
    'fish',
    'sleep',
    'search_water',
    'explore',
    # Events
    'generate_event',
    # Save system
    'save_game',
    'load_game',
    'delete_save',
    # Game management
    'game_loop',
    'display_gauges',
    'choose_action',
    'check_conditions',
]

__version__ = '1.0.0'
__author__ = 'LoicAND'
