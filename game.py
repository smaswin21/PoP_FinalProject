# game.py
# In this file the GUI of the game will be defined here

import pygame, sys
from character import Character
from chest import Chest
from room import Room
from entities import Entities

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
ROOM_WIDTH = 400
ROOM_HEIGHT = 400

# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class FrontEndCharacter(pygame.sprite.Sprite):
    def __init__(self, picture_path, character: Character):
        super().__init__()
        self.character = character
        self.image = pygame.image.load(picture_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (character.getWidth(), character.getHeight())) 
        self.rect = self.image.get_rect()
        self.rect.x = character.getX_Coordinate()
        self.rect.y = character.getY_Coordinate()
        
    # Move the sprite based on user keypresses
    def update(self):
        self.rect.x = self.character.getX_Coordinate()
        self.rect.y = self.character.getY_Coordinate()
        
class FrontEndChest(pygame.sprite.Sprite):
    def __init__(self, picture_path, chest: Chest):
        super().__init__()
        self.chest = chest
        self.image = pygame.image.load(picture_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (chest.getWidth(), chest.getHeight()))
        self.rect = self.image.get_rect()
        self.rect.x = chest.getX_Coordinate()
        self.rect.y = chest.getY_Coordinate()
        
    def update(self):
        pass
    
class FrontEndEntity(pygame.sprite.Sprite):
    def __init__(self, picture_path, entity):
        super().__init__()
        self.entity = entity
        self.image = pygame.image.load(picture_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (entity.getWidth(), entity.getHeight()))
        self.rect = self.image.get_rect()
        self.rect.x = entity.getX_Coordinate()
        self.rect.y = entity.getY_Coordinate()
        
    def update(self):
        pass

# TODO: Keep this here and move other methods to a frontend.py file
class Game():
    def __init__(self, labyrinth: Entities, SCREEN_WIDTH: int, SCREEN_HEIGHT: int):
        pygame.init()
        self.labyrinth = labyrinth
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.backend_character = Character("Bob", health=3, inventory=[], 
                                           score=0, x_coordinate=0, y_coordinate=0,
                                           width=50, height=50)
        self.frontend_character = FrontEndCharacter("assets/player.png", self.backend_character)
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                
    def update(self, dt):
        keys_pressed = pygame.key.get_pressed()
        self.backend_character.update(keys_pressed, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.frontend_character.update()
        
    def draw(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.frontend_character.image, self.frontend_character.rect)
        pygame.display.flip()
    
    def createFrontEndEntity(self):
        for room in labyrinth:
            room

# TODO: Put this in run method
if __name__ == "__main__":
    #Initalise Game Object (controller)
    entities = Entities(5)
    labyrinth = entities.createLabyrinth()
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
    
    # Game loop
    clock = pygame.time.Clock()
    running = True
    while running:
        # Handle events
        game.handle_events()
        
        # Update game state
        dt = clock.tick(60) / 1000.0
        game.update(dt)
        
        # Draw the screen
        game.draw()
