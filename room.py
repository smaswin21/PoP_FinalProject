# room.py
# This file contains the room class of each room that will be put
# in the labyrinth

class Room:
    def __init__(self, items, chests, traps):
        self.dimensions = [400, 400]
        self.items = items
        self.chests = chests
        self.traps = traps

    # Getter methods
    def getDimensions(self):
        return self.dimensions

    def getItems(self):
        return self.items
    
    # TODO change return value to Item array
    def getChests(self):
        return self.chests
    
    def getTraps(self):
        return self.traps
    
    # Setter methods
    def setName(self, dimensions):
        self.dimensions = dimensions

    def setHealth(self, items):
        self.items = items
    
    def setChests(self, chests):
        self.chests = chests
    
    def setScore(self, traps):
        self.traps = traps