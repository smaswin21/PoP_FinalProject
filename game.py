# game.py
# In this file we have the game class where all entities will 
# be created and the character will be able to move through
# the labyrinth
# TODO: This class is not done might reuse to organise my method in run better
from entities import Entities
from character import Character

class Game:
    def __init__(self, rooms, character: Character) -> None:
        self.rooms = rooms
        self.character = character
    
    def characterMoveInput(self, character: Character):
        prompt = input("Where would you like to move?   (right, left, up, down)").lower()
        character.move(prompt)
        
    def enterRoom(self):
        character = self.character
        room = self.rooms
        while character.getPosition() != room.getExit():
            print("Exit is at: ", room.getExit())
            print("You are at position: ", character.getPosition())
            prompt = input("Where would you like to move?   (right, left, up, down)")
            
            character.move(prompt.lower())
        
        character.setPosition([0, 0])
        print("Congrats you are onto the next room!")
