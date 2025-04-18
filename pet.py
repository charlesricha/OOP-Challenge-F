class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # Start with moderate hunger
        self.energy = 5   # Start with moderate energy
        self.happiness = 5  # Start with moderate happiness
        self.tricks = []    # List to store learned tricks
    
    def eat(self):
        """Reduces hunger and increases happiness"""
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} eats happily. Hunger decreases, happiness increases!")
    
    def sleep(self):
        """Increases energy level"""
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} takes a nap. Energy restored!")
    
    def play(self):
        """Changes multiple attributes through play"""
        if self.energy < 2:
            print(f"{self.name} is too tired to play right now.")
            return
        
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        print(f"{self.name} plays excitedly! Energy decreases, but happiness increases.")
    
    def train(self, trick):
        """Teaches the pet a new trick"""
        if self.energy < 3:
            print(f"{self.name} is too tired to learn right now.")
            return
        
        self.tricks.append(trick)
        self.energy = max(0, self.energy - 1)
        self.hunger = min(10, self.hunger + 1)
        print(f"Congratulations! {self.name} learned to {trick}!")
    
    def show_tricks(self):
        """Displays all learned tricks"""
        if not self.tricks:
            print(f"{self.name} hasn't learned any tricks yet.")
        else:
            print(f"{self.name} knows these tricks:")
            for i, trick in enumerate(self.tricks, 1):
                print(f"{i}. {trick}")
    
    def get_status(self):
        """Prints the current state of the pet"""
        print("\n" + "="*30)
        print(f"{self.name}'s Current Status:")
        print(f"Hunger: {'★ ' * self.hunger}{'☆ ' * (10 - self.hunger)} ({self.hunger}/10)")
        print(f"Energy: {'★ ' * self.energy}{'☆ ' * (10 - self.energy)} ({self.energy}/10)")
        print(f"Happiness: {'★ ' * self.happiness}{'☆ ' * (10 - self.happiness)} ({self.happiness}/10)")
        print("="*30 + "\n")