# character.py
# This file contains the character class of the playable character
# in game

from item import Item

class Character:
    def __init__(self, name, health, inventory, score, position):
        self.name = name
        self.health = health
        self.inventory = inventory
        self.score = score
        self.position = position

    # Function that can move player in position array either right, left
    # up, down
    def move(self, direction: str, size: int):
        try:
            if (direction == "right"): self.position[0] += size
            if (direction == "left"): self.position[0] -= size
            if (direction == "up"): self.position[1] += size
            if (direction == "down"): self.position[1] -= size
        except:
            print("Invalid move try again")
    
    # The puzzle of the game, returns true if the character has 3 legendary
    # items       
    def checkEasterEgg(self) -> bool:
        inventory = self.getInventory()
        legendaries = []
        for item in inventory:
            if len(legendaries) == 3: return True
            if item.getRarity() == "Legendary":
                legendaries.append(item)
        
        return False
    
    # Checks to see if chosen item exits in character inventory
    def findItemInInventory(self, chosen: str) -> Item:
        inventory = self.getInventory()
        for item in inventory:
            if chosen.lower() == item.getName().lower():
                return item
        
        raise ValueError("Item does not exist")
    
    # Looks through all rarity values of items in inventory and adjusts score
    def changeScore(self):
        inventory = self.inventory
        score = 0
        for item in inventory:
            score += item.rarityPoints()
        self.setScore(score)
            
    # Add item to inventory
    def addItem(self, item):
        self.inventory.append(item)

    # Remove item from inventory
    def removeItem(self, item):
        self.inventory.remove(item)

    # Remove damage for player health bar
    def removeHealth(self, num):
        self.setHealth(self.getHealth() - num)

    # Getter methods
    def getName(self) -> str:
        return self.name

    def getHealth(self) -> int:
        return self.health
    
    def getInventory(self):
        return self.inventory
    
    def getScore(self) -> int:
        return self.score
    
    # TODO change return value to int array
    def getPosition(self):
        return self.position
    
    # Setter methods
    def setName(self, name):
        self.name = name

    def setHealth(self, health):
        self.health = health
    
    def setInventory(self, inventory):
        self.inventory = inventory
    
    def setScore(self, score):
        self.score = score
    
    def setPosition(self, position):
        self.position = position


    

