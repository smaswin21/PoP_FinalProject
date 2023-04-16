# room.py
# This file contains the room class of each room that will be put
# in the labyrinth

class Room:
    def __init__(self, name, dimensions, items, chests, traps):
        self.name = name
        self.dimensions = dimensions
        self.items = items
        self.chests = chests
        self.traps = traps

    # Getter methods
    def getName(self):
        return self.name

    def getDimensions(self):
        return self.dimensions

    def getItems(self):
        return self.items
    
    def getChests(self):
        return self.chests
    
    def getTraps(self):
        return self.traps
    
    # Setter methods
    def setName(self, name):
        self.name = name

    def setDimensions(self, dimensions):
        self.dimensions = dimensions

    def setItems(self, items):
        self.items = items
    
    def setChests(self, chests):
        self.chests = chests
    
    def setScore(self, traps):
        self.traps = traps