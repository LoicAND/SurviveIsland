class Player:
    
    def __init__(self, hunger=100, thirst=100, energy=100, days_survived=0):
        self.hunger = hunger
        self.thirst = thirst
        self.energy = energy
        self.days_survived = days_survived
    
    def update_gauges(self, delta_hunger=0, delta_thirst=0, delta_energy=0):
        self.hunger = max(0, min(100, self.hunger + delta_hunger))
        self.thirst = max(0, min(100, self.thirst + delta_thirst))
        self.energy = max(0, min(100, self.energy + delta_energy))
    
    def is_alive(self):
        return self.hunger > 0 and self.thirst > 0 and self.energy > 0
    
    def display_status(self):
        print("=" * 40)
        print("PLAYER STATUS")
        print("=" * 40)
        print(f"Hunger   : {self.hunger}/100")
        print(f"Thirst   : {self.thirst}/100")
        print(f"Energy   : {self.energy}/100")
        print(f"Days survived : {self.days_survived}")
        print("=" * 40)
        
        if not self.is_alive():
            print("⚠️  ALERT: Player is in critical danger!")
            print("=" * 40)
