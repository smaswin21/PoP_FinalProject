# trap.py
# This file contains the trap class for each trap in the game
# that comes in different sizes and damages the player

class Trap:
    def __init__(self, size, damage) -> None:
        self.size = size
        self.damage = damage
        self.position = [0, 0]

    # Getter methods
    def getSize(self):
        return self.size

    def getDamage(self) -> int:
        return self.damage
    
    def getPosition(self):
        return self.position
    
     # Setter methods
    def setSize(self, size):
        self.size = size

    def setDamage(self, damage):
        self.damage = damage
        
    def setPosition(self, position):
        self.position = position