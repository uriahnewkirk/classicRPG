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
        self.font = pygame.font.Font("C:/Windows/Fonts/Arial.ttf", 96)

        #declare our spritesheet variables
        self.character_spritesheet = Spritesheet('assets/Characters/BirdBlue/BIRDSPRITESHEET_Blue.png')
        self.tileset32Rogues_spritesheet = Spritesheet('assets/Terrain/32rogues_tiles.png')
        self.enemy_spritesheet = Spritesheet("assets/Characters/CatGrey/CATSPRITESHEET_Gray.png")
        self.attack_spritesheet = Spritesheet("assets/FX/SlashCurved.png")
        self.intro_background = pygame.image.load("./assets/HUD/intro_Background.png")
        self.gameOverBackground = pygame.image.load("./assets/HUD/gameOverBackground.png")

    def createTilemap(self):
        #enumerate helps iterate through the 2d array
        for w, row in enumerate(tilemap):
            for i, column in enumerate(row):
                Ground(self, i, w)
                if column == "B":
                    Block(self, i, w)
                if column == "P":
                    # Player(self, i, w)
                    self.player = Player(self, i, w)
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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.player.facing == "up":
                        Attack(self, self.player.rect.x, self.player.rect.y - TILESIZE)
                    if self.player.facing == "down":
                        Attack(self, self.player.rect.x, self.player.rect.y + TILESIZE)
                    if self.player.facing == "left":
                        Attack(self, self.player.rect.x - TILESIZE, self.player.rect.y)
                    if self.player.facing == "right":
                        Attack(self, self.player.rect.x + TILESIZE, self.player.rect.y)

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
        # self.running = False

    def game_over(self):
        text = self.font.render("Game Over!", True, "#E7E7E7")
        textRect = text.get_rect(center=(WIN_WIDTH/2, WIN_HEIGHT/2))
        restartButton = Button(640/2 - 60, 480/2 + 60, 150, 50, "#E7E7E7", "#000000", "Restart", 32) #manually positioned based on static game window size

        for sprite in self.all_sprites:
            sprite.kill()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            mousePos = pygame.mouse.get_pos()
            mousePressed = pygame.mouse.get_pressed()

            if restartButton.isPressed(mousePos, mousePressed):
                self.new()
                self.main()

            self.screen.blit(self.gameOverBackground, (0,0))
            self.screen.blit(text, textRect)
            self.screen.blit(restartButton.image, restartButton.rect)
            self.clock.tick(FPS)
            pygame.display.update()

    def intro_screen(self):
        intro = True

        title = self.font.render("Classic RPG", True, "#E7E7E7") #manually positioned based on static game window size
        titleRect = title.get_rect(x = 50, y = 50)
        playButton = Button(640/2 - 50, 480/2 - 50, 100, 50, "#E7E7E7", "#005D24", "Play", 32)

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False
            
            mousePos = pygame.mouse.get_pos()
            mousePressed = pygame.mouse.get_pressed()

            if playButton.isPressed(mousePos, mousePressed):
                intro = False

            self.screen.blit(self.intro_background, (0,0))
            self.screen.blit(title, titleRect)
            self.screen.blit(playButton.image, playButton.rect)
            self.clock.tick(FPS)
            pygame.display.update()

#initial start of the program/game
g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()