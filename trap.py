# trap.py
# This file contains the trap class for each trap in the game
# that comes in different sizes and damages the player

class Trap:
    def __init__(self, damage, width, height, x_coordinate=None, y_coordinate=None):
        self.damage = damage
        self.width = width
        self.height = height
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    # Getter methods
    def getSize(self):
        return self.size

    def getDamage(self) -> int:
        return self.damage
    
    def getX_Coordinate(self) -> int:
        return self.x_coordinate
    
    def getY_Coordinate(self) -> int:
        return self.y_coordinate
    
    def getWidth(self) -> int:
        return self.width
    
    def getHeight(self) -> int:
        return self.height
    
     # Setter methods
    def setSize(self, size):
        self.size = size

    def setDamage(self, damage):
        self.damage = damage
        
    def setX_Coordinate(self, x_coordinate):
        self.x_coordinate = x_coordinate
        
    def setY_Coordinate(self, y_coordinate):
        self.y_coordinate = y_coordinate
        
    def setWidth(self, width):
        self.width = width
    
    def setHeight(self, height):
        self.height = height