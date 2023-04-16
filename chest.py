# chest.py
# This file contains the chest class for each chest in game

from item import Item

class Chest:
    def __init__(self, name, item):
        self.name = name
        self.item = item

    # Getter methods
    def getName(self) -> str:
        return self.name

    def getItem(self) -> Item:
        return self.item
    
     # Setter methods
    def setName(self, name):
        self.name = name

    def setItem(self, item):
        self.item = item
    

    

    

    
    



    

    
        