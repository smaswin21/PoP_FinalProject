# game.py
# In this file we have the game class where all entities will 
# be created and the character will be able to move through
# the labyrinth
# TODO: This class is not done might reuse to organise my method in run better
from entities import Entities
from character import Character
from chest import Chest
from item import Item
from trap import Trap
from room import Room

class Game:
    def __init__(self, rooms, character: Character) -> None:
        self.rooms = rooms
        self.character = character
    
    def characterMoveInput(self, character: Character):
        prompt = input("Where would you like to move?   (right, left, up, down)").lower()
        character.move(prompt)
        
    # Prompt for interacting with chest entity
    def foundChest(character: Character, chest: Chest):
        while True:
            print("")
            print("!!!")
            prompt = input("You have found a chest would you like to open it? (y/n)")
            print("")
            
            if prompt.lower() == "y":
                if chest.getItem() != None:
                    character.addItem(chest.getItem())
                    
                    # Updating score with new item
                    score = character.getScore()
                    character.setScore(score + item.rarityPoints())  
                    
                    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                    print("You just picked up: ", chest.getItem().getName(), " (", chest.getItem().getName(), ")")
                    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                    print()
                    chest.setItem(None)
                    return
                print("Sorry you already took this item from the chest!")
                return
            elif prompt.lower() == "n":
                print("?????????????????????????????????????")
                print("Missing out on something good here...")
                print("?????????????????????????????????????")
                return
            else:
                print("Not a valid input, it is y/n")
                
    # Prompt for interacting with item entity       
    def foundItem(character: Character, item: Item):
        while True:
            print("")
            print("!!!")
            prompt = input("You have found an item! Would you like to pick it up? (y/n)")
            print("")
            
            if prompt.lower() == "y":
                character.addItem(item)
                
                # Updating score with new item
                score = character.getScore()
                character.setScore(score + item.rarityPoints())  
                
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                print("You just picked up: ", item.getName())
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                return
            elif prompt.lower() == "n":
                print("?????????????????????????????????????")
                print("Missing out on something good here...")
                print("?????????????????????????????????????")
                return
            else:
                print("Not a valid input, it is y/n")

    # Prompt for interacting with item trap 
    def foundTrap(character: Character, trap: Trap):
        damage = trap.getDamage()
        character.removeHealth(damage)
        print("")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("Oh no you have walked into a trap and you have been damaged by 1 heart!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("")
        
    # Checks to see if character has encountered any entity, if so an interaction 
    # will occur with its suitable entity 
    def findEntity(character: Character, entity_mapping):
        character_position = character.getPosition()
        # To avoid iteration size changed in dictionnary during runtime
        entity_mapping_temp = dict(entity_mapping)  
        
        for entity in entity_mapping_temp:
            position = entity_mapping[entity]
            if position == character_position:
                if isinstance(entity, Chest):
                    foundChest(character, entity)
                elif isinstance(entity, Item):
                    foundItem(character, entity)
                    del entity_mapping[entity]
                elif isinstance(entity, Trap):
                    foundTrap(character, entity)
                else:
                    raise NameError("Invalid type of entity")
        
                
    # Map any entity to their respective position in the room            
    def mapEntities(entities):
        entity_mapping = {}
        for entity in entities:
            print(type(entity).__name__, " at ", entity.getPosition())
            entity_mapping[entity] = entity.getPosition()
        
        return entity_mapping
    # Main logic for all actions that will happen when a character is inside a room
    def enterRoom(character: Character, room: Room):
        # Mapping all entities with their respective location
        chest_mapping = mapEntities(room.getChests())
        trap_mapping = mapEntities(room.getTraps())
        item_mapping = mapEntities(room.getItems())
        
        while character.getPosition() != room.getExit():
            print("Exit is at: ", room.getExit())
            print("You are at position: ", character.getPosition())
            
            # Checking to see if character has encountered an entity in the game
            findEntity(character, chest_mapping)
            findEntity(character, trap_mapping)
            findEntity(character, item_mapping)
            
            # Displaying user information
            inventory = character.getInventory()
            health = character.getHealth()
            score = character.getScore()
            try:
                print("Inventory: ")
                for item in inventory:
                    print(item.getName(), end=" | ")
            except:
                print("Inventory: None")
            print("\nHealth: ", health)
            print("Score: ", score)
            
            # Prompting user to move character in the room
            prompt = input("Where would you like to move?   (right, left, up, down)")
            character.move(prompt.lower())
            
        character.setPosition([0, 0])
        print("")
        print("************************************")
        print("Congrats you are onto the next room!")
        print("************************************")
        print("")
