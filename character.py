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
    def move(self, direction: str):
        try:
            if (direction == "right"): self.position[0] += 1
            if (direction == "left"): self.position[0] -= 1
            if (direction == "up"): self.position[1] += 1
            if (direction == "down"): self.position[1] -= 1
        except:
            print("Invalid move try again")
            

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


    

