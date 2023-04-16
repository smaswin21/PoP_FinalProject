# labyrinth.py
# This file contains the class labyrinth. It will create the labyrinth
# With all the entities inside it (Character, Room, Chest, Trap, Item)
# Note that rarity chance is C:50%, R:30%, E:20%, L:10%
import random
from chest import Chest
from trap import Trap
from room import Room
from item import Item

class Labyrinth:
    def __init__(self, roomcount: int):
        self.roomcount = roomcount

    # Creating all the items in the game
    def defineItems(self):
        paper = Item("Piece of paper", "Common")
        rock = Item("Rock", "Common")
        scissors = Item("Scissors", "Common")
        silver = Item("Silver ingot", "Rare")
        iron = Item("Iron ingot", "Rare")
        copper = Item("Copper ingot", "Rare")
        amulet = Item("Amulet", "Epic")
        medalion = Item("Medalion", "Epic")
        trophy = Item("Trophy", "Epic")
        wand = Item("Wand", "Legendary")
        emerald = Item("Emerald", "Legendary")
        pandora = Item("Pandora's box", "Legendary")

        # Sorting out the items into 3 different lists of rarity
        common_items = [paper, rock, scissors]
        rare_items = [silver, iron, copper]
        epic_items =[amulet, medalion, trophy]
        legendary_items = [wand, emerald, pandora]

        return common_items, rare_items, epic_items, legendary_items

    # Method to create a chest with random chance to have epic or legendary
    def createChest(self, epic, legendary) -> Chest:
        choices = [epic, legendary]
        rarity = random.choices(choices, weights=(20, 10), k=1)
        
        # Rarity is returned as a list so as 2 choices we return element 0 and
        # rarity is a list of the n items in their rarity category so we choose
        # one item randomly with equal weighted probability
        items = rarity[0]
        item = items[random.randint(0, len(items)-1)]
        chest = Chest("chest", item)   

        return chest
    
    # Method to create trap with random chance of its size
    def createTrap(self) -> Trap:
        # Default trap size will only be width and length 2 - 4
        w = random.choice([2, 4])
        l = random.choice([2, 4])
        size = [w, l]

        # Default damage for trap is 1 health for the character
        trap = Trap(size, 1)

        return trap
    
    # Method to create n rooms in the labyrinth
    def createRooms(self, n, maxChests, maxTraps, maxItems):
        # Invoking all the items in the game
        common_items, rare_items, epic_items, legendary_items = self.defineItems()
        all_items = [common_items, rare_items, epic_items, legendary_items]
        
        # Generating entities for n rooms
        rooms = []
        for i in range(n):

            # Making 0 - 3 chests with random items inside
            chests = []
            for j in range(random.randint(0, maxChests)):
                chests.append(self.createChest(epic_items, legendary_items))
                
            #print(chests[0].getName())
            
            # Making 0 - 3 traps with random width and length of max values 2 or 4
            traps = []
            for j in range(random.randint(0, maxTraps)):
                traps.append(self.createTrap())

            # Choosing 0 - 4 items with respective weightings
            items = []
            rarities = random.choices(all_items, weights=(50, 30, 20, 10), k=maxItems)

            # Made a list of all items with their rarity, now take a random item from 
            # rarity category with equal weighting
            for item in rarities:
                items.append(item[random.randint(0, len(item)-1)])

            # Creating Room object with all entities
            room = Room("Room" + str(i), [100, 100], items, chests, traps)
            rooms.append(room)

            #################
            ###debug code####
            #################

            #for room in rooms:
                #print(room.getName(), " with item: ", room.getChests()[0].getItem().getName())

            #################
            ###/debug code###
            #################

        return rooms

    # Create full labyrinth with n rooms
    def createLabyrinth(self):
        labyrinth = self.createRooms(self.getRoomCount(), maxChests=3, maxTraps=3, maxItems=4)

        return labyrinth
    
    # Getter methods
    def getRoomCount(self) -> int:
        return self.roomcount
    
    # Setter methods
    def setRoomCount(self, roomcount):
        self.roomcount = roomcount
    

