class Player:
    """
    Represents the player in the survival game.
    
    Manages the player's vital statistics (hunger, thirst, energy) 
    and tracks survival progress.
    """
    
    def __init__(self, hunger=100, thirst=100, energy=100, days_survived=0, name="Survivor"):
        """
        Initialize a new player.
        
        Args:
            hunger (int): Initial hunger level (0-100, default: 100)
            thirst (int): Initial thirst level (0-100, default: 100)
            energy (int): Initial energy level (0-100, default: 100)
            days_survived (int): Number of days survived (default: 0)
            name (str): Player's name (default: "Survivor")
        """
        self.name = name
        self.hunger = hunger
        self.thirst = thirst
        self.energy = energy
        self.days_survived = days_survived
    
    def update_gauges(self, delta_hunger=0, delta_thirst=0, delta_energy=0):
        """
        Update the player's vital statistics.
        
        Ensures all values stay within the valid range (0-100).
        
        Args:
            delta_hunger (int): Change in hunger level (negative = increase hunger)
            delta_thirst (int): Change in thirst level (negative = increase thirst)
            delta_energy (int): Change in energy level (negative = decrease energy)
        """
        self.hunger = max(0, min(100, self.hunger + delta_hunger))
        self.thirst = max(0, min(100, self.thirst + delta_thirst))
        self.energy = max(0, min(100, self.energy + delta_energy))
    
    def is_alive(self):
        """
        Check if the player is still alive.
        
        Returns:
            bool: True if all vital stats are above 0, False otherwise
        """
        return self.hunger > 0 and self.thirst > 0 and self.energy > 0
    
    def display_status(self):
        """
        Display the player's current status in a formatted way.
        
        Shows name, all vital statistics, and days survived.
        Displays a warning if the player is in critical danger.
        """
        print("=" * 40)
        print(f"🏝️  {self.name.upper()}'S STATUS")
        print("=" * 40)
        print(f"Hunger   : {self.hunger}/100")
        print(f"Thirst   : {self.thirst}/100")
        print(f"Energy   : {self.energy}/100")
        print(f"Days survived : {self.days_survived}")
        print("=" * 40)
        
        if not self.is_alive():
            print("⚠️  ALERT: Player is in critical danger!")
            print("=" * 40)
