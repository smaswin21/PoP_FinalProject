from entities import Entities
from game import Game
from character import Character

# Goal of game: Go through labyrinth with 5 rooms and try to pick up many items as possible.
# Each item will have a rarity, each rarity will correspond to a number of points. There are
# traps and chests along the way to either improve chance of picking up good item or dying
# before the finish line. You can fuse 2 items to get one with higher rarity and get more points.
# Character will have 3 lives each trap will take off 1 life. Will allow player to fuse 2 items 
# with the same rarity. If you get 3 legendaries, automatically end the run you have won.
# Chests will only have epic or legendary items

def enterRoom(character, room):
        while character.getPosition() != room.getExit():
            print("Exit is at: ", room.getExit())
            print("You are at position: ", character.getPosition())
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
    character = Character("Bob", 3, None, 0)
    
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
            print("Position in room: ", chest.getPosition())
            
        print("-----------------------")
        print("You")
        print("-----------------------")
        
        enterRoom(character, room)

    print("/////////////////////////")
    print("End of Game")
    print("/////////////////////////")
