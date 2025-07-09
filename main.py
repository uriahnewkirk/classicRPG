import pygame
from sprites import *
from config import *
import sys


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        #declare our spritesheet variables
        self.character_spritesheet = Spritesheet('assets/Characters/BirdBlue/BIRDSPRITESHEET_Blue.png')
        self.tileset32Rogues_spritesheet = Spritesheet('assets/Terrain/32rogues_tiles.png')
        self.enemy_spritesheet = Spritesheet("assets/Characters/CatGrey/CATSPRITESHEET_Gray.png")

    def createTilemap(self):
        #enumerate helps iterate through the 2d array
        for w, row in enumerate(tilemap):
            for i, column in enumerate(row):
                Ground(self, i, w)
                if column == "B":
                    Block(self, i, w)
                if column == "P":
                    Player(self, i, w)
                if column == "G":
                    Grass(self, i, w)
                if column == "T":
                    TopWall(self, i, w)
                if column == "O":
                    Obstacle01(self, i, w)
                if column == "D":
                    Obstacle02(self, i, w)
                if column == "E":
                    Enemy(self, i, w)
    
    def new(self):
        #starting a new game
        self.playing = True

        #object containing all game sprites
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()
        self.createTilemap()

    def events(self):
        #gameplay events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        #gameplay update
        self.all_sprites.update()

    def draw(self):
        #gameplay drawings
        self.screen.fill("#111111")
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        #gameplay loop
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False

    def game_over(self):
        pass

    def intro_screen(self):
        pass

#initial start of the program/game
g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()