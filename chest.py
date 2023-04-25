# chest.py
# This file contains the chest class for each chest in game

from item import Item

class Chest:
    def __init__(self, name, item, width, height, x_coordinate=None, y_coordinate=None):
        self.name = name
        self.item = item
        self.width = width
        self.height = height
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    # Getter methods
    def getName(self) -> str:
        return self.name

    def getItem(self) -> Item:
        return self.item
    
    def getX_Coordinate(self) -> int:
        return self.x_coordinate
    
    def getY_Coordinate(self) -> int:
        return self.y_coordinate
    
    def getWidth(self) -> int:
        return self.width
    
    def getHeight(self) -> int:
        return self.height
    
     # Setter methods
    def setName(self, name):
        self.name = name

    def setItem(self, item):
        self.item = item
    
    def setX_Coordinate(self, x_coordinate):
        self.x_coordinate = x_coordinate
        
    def setY_Coordinate(self, y_coordinate):
        self.y_coordinate = y_coordinate
        
    def setWidth(self, width):
        self.width = width
    
    def setHeight(self, height):
        self.height = height
    

    

    

    
    



    

    
        