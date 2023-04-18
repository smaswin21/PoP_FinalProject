from entities import Entities
from game import Game
from character import Character
from chest import Chest
from trap import Trap
from item import Item
from room import Room

# Goal of game: Go through labyrinth with 5 rooms and try to pick up many items as possible.
# Each item will have a rarity, each rarity will correspond to a number of points. There are
# traps and chests along the way to either improve chance of picking up good item or dying
# before the finish line. You can fuse 2 items to get one with higher rarity and get more points.
# Character will have 3 lives each trap will take off 1 life. Will allow player to fuse 2 items 
# with the same rarity. If you get 3 legendaries, automatically end the run you have won.
# Chests will only have epic or legendary items

# TODO: Put all of these functions into new class called Game

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

# Below is only test code for now
if __name__ == "__main__":
    entities = Entities(5)
    labyrinth = entities.createLabyrinth()
    character = Character("Bob", 3, [], 0, [0, 0])
    
    print("/////////////////////////")
    print("Start of Game")
    print("/////////////////////////")

    for room in labyrinth:
        print("-----------------------")
        print("-> ", room.getName())
        print("Room dimensions: ", room.getDimensions())
        print("Exit Position: ", room.getExit())
        print("-----------------------")
        print("-----------------------")
        print("Items")
        print("-----------------------")
        
        for item in room.getItems():
            print("Name: ", item.getName())
            print("Rarity: ", item.getRarity())
            print("Position in room: ", item.getPosition())
            
        print("-----------------------")
        print("Chests")
        print("-----------------------")
        
        for chest in room.getChests():
            print("Item in chest: ", chest.getItem().getName())
            print("Rarity in chest: ", chest.getItem().getRarity())
            print("Position in room: ", chest.getPosition())
            
        print("-----------------------")
        print("Traps")
        print("-----------------------")
        
        for trap in room.getTraps():
            print("Trap here at: ", trap.getSize())
            print("Position in room: ", trap.getPosition())
            
        print("-----------------------")
        print("You")
        print("-----------------------")
        
        enterRoom(character, room)
    
    print("")
    print("**************************************************")
    print("Congrats! you have made it throught the labyrinth.")
    print("**************************************************")
    print("")
    print("Your final score was: ", character.getScore())

    print("/////////////////////////")
    print("End of Game")
    print("/////////////////////////")
