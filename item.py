# item.py
# This file contains the item class for each item that will be picked up in the game
# in game

class Item:
    def __init__(self, name, rarity):
        self.name = name
        self.rarity = rarity

    # Returns the points value for the item
    def rarityPoints(self) -> int:
        # Rarity with corresponding points
        rarity_points = {
            "Common": 10,
            "Rare": 30,
            "Epic": 50,
            "Legendary": 100
        }
        return rarity_points[self.rarity]

    # Getter methods
    def getName(self) -> str:
        return self.name

    def getRarity(self) -> str:
        return self.rarity
    
     # Setter methods
    def setName(self, name):
        self.name = name

    def setRarity(self, rarity):
        self.rarity = rarity
    

    

    

    
    



    

    
        