from labyrinth import Labyrinth

# Goal of game: Go through labyrinth with 5 rooms and try to pick up many items as possible.
# Each item will have a rarity, each rarity will correspond to a number of points. There are
# traps and chests along the way to either improve chance of picking up good item or dying
# before the finish line. You can fuse 2 items to get one with higher rarity and get more points.
# Character will have 3 lives each trap will take off 1 life. Will allow player to fuse 2 items 
# with the same rarity. If you get 3 legendaries, automatically end the run you have won.
# Chests will only have epic or legendary items

# Below is only test code for now
if __name__ == "__main__":
    test = Labyrinth(5)
    labyrinth = test.createLabyrinth()
    print("/////////////////////////")
    print("Your labyrinth generation")
    print("/////////////////////////")

    for room in labyrinth:
        print("-----------------------")
        print("-> ", room.getName())
        print("-----------------------")
        print("-----------------------")
        print("Items")
        print("-----------------------")
        
        for item in room.getItems():
            print("Name: ", item.getName())
            print("Rarity: ", item.getRarity())
            
        print("-----------------------")
        print("Chests")
        print("-----------------------")
        
        for chest in room.getChests():
            print("Item in chest: ", chest.getItem().getName())
            print("Rarity in chest: ", chest.getItem().getRarity())
            
        print("-----------------------")
        print("Traps")
        print("-----------------------")
        
        for trap in room.getTraps():
            print("Trap here at: ", trap.getSize())

    print("/////////////////////////")
    print("Done labyrinth generation")
    print("/////////////////////////")
    
    print(test.getRoomCount())
