import pygame
from config import *
import math
import random


class Spritesheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def getSprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0,0), (x, y, width, height))
        sprite.set_colorkey("#000000")
        return sprite


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = player_layer
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        #handle change in movement
        self.x_change = 0
        self.y_change = 0

        self.facing = 'down' #direction of player sprite
        self.animationLoop = 1

        self.image = self.game.character_spritesheet.getSprite(0, 0, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.movement()
        self.animate()
        self.rect.x += self.x_change
        self.collideBlocks("x")
        self.rect.y += self.y_change
        self.collideBlocks("y")
        self.collideEnemy()

        #calculate the change in velocity
        self.x_change = 0
        self.y_change = 0
    
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            # for sprite in self.game.all_sprites:
            #     sprite.rect.x += player_speed
            self.x_change -= player_speed
            self.facing = 'left'
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            # for sprite in self.game.all_sprites:
            #     sprite.rect.x -= player_speed
            self.x_change += player_speed
            self.facing = 'right'
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            # for sprite in self.game.all_sprites:
            #     sprite.rect.y -= player_speed
            self.y_change += player_speed
            self.facing = 'down'
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            # for sprite in self.game.all_sprites:
            #     sprite.rect.y += player_speed
            self.y_change -= player_speed
            self.facing = 'up'

    def collideBlocks(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right

        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom

    def collideEnemy(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemies, False)
        if hits:
            self.kill()
            self.game.playing = False

    def animate(self):
        downI_animations = [self.game.character_spritesheet.getSprite(0, 0, self.width, self.height),
                           self.game.character_spritesheet.getSprite(32, 0, self.width, self.height),
                           self.game.character_spritesheet.getSprite(64, 0, self.width, self.height),
                           self.game.character_spritesheet.getSprite(96, 0, self.width, self.height),
                           self.game.character_spritesheet.getSprite(0, 0, self.width, self.height),
                           self.game.character_spritesheet.getSprite(32, 0, self.width, self.height),
                           self.game.character_spritesheet.getSprite(64, 0, self.width, self.height),
                           self.game.character_spritesheet.getSprite(96, 0, self.width, self.height)]
        
        down_animations = [self.game.character_spritesheet.getSprite(0, 160, self.width, self.height),
                           self.game.character_spritesheet.getSprite(32, 160, self.width, self.height),
                           self.game.character_spritesheet.getSprite(64, 160, self.width, self.height),
                           self.game.character_spritesheet.getSprite(96, 160, self.width, self.height),
                           self.game.character_spritesheet.getSprite(0, 192, self.width, self.height),
                           self.game.character_spritesheet.getSprite(32, 192, self.width, self.height),
                           self.game.character_spritesheet.getSprite(64, 192, self.width, self.height),
                           self.game.character_spritesheet.getSprite(96, 192, self.width, self.height),]
        
        upI_animations = [self.game.character_spritesheet.getSprite(0, 96, self.width, self.height),
                           self.game.character_spritesheet.getSprite(32, 96, self.width, self.height),
                           self.game.character_spritesheet.getSprite(64, 96, self.width, self.height),
                           self.game.character_spritesheet.getSprite(96, 96, self.width, self.height),
                           self.game.character_spritesheet.getSprite(0, 96, self.width, self.height),
                           self.game.character_spritesheet.getSprite(32, 96, self.width, self.height),
                           self.game.character_spritesheet.getSprite(64, 96, self.width, self.height),
                           self.game.character_spritesheet.getSprite(96, 96, self.width, self.height),]

        up_animations = [self.game.character_spritesheet.getSprite(0, 352, self.width, self.height),
                           self.game.character_spritesheet.getSprite(32, 352, self.width, self.height),
                           self.game.character_spritesheet.getSprite(64, 352, self.width, self.height),
                           self.game.character_spritesheet.getSprite(96, 352, self.width, self.height),
                           self.game.character_spritesheet.getSprite(0, 384, self.width, self.height),
                           self.game.character_spritesheet.getSprite(32, 384, self.width, self.height),
                           self.game.character_spritesheet.getSprite(64, 384, self.width, self.height),
                           self.game.character_spritesheet.getSprite(96, 384, self.width, self.height),]
        
        leftI_animations = [self.game.character_spritesheet.getSprite(0, 64, self.width, self.height),
                           self.game.character_spritesheet.getSprite(32, 64, self.width, self.height),
                           self.game.character_spritesheet.getSprite(64, 64, self.width, self.height),
                           self.game.character_spritesheet.getSprite(96, 64, self.width, self.height),
                           self.game.character_spritesheet.getSprite(0, 64, self.width, self.height),
                           self.game.character_spritesheet.getSprite(32, 64, self.width, self.height),
                           self.game.character_spritesheet.getSprite(64, 64, self.width, self.height),
                           self.game.character_spritesheet.getSprite(96, 64, self.width, self.height),]
        
        left_animations = [self.game.character_spritesheet.getSprite(0, 224, self.width, self.height),
                           self.game.character_spritesheet.getSprite(32, 224, self.width, self.height),
                           self.game.character_spritesheet.getSprite(64, 224, self.width, self.height),
                           self.game.character_spritesheet.getSprite(96, 224, self.width, self.height),
                           self.game.character_spritesheet.getSprite(0, 256, self.width, self.height),
                           self.game.character_spritesheet.getSprite(32, 256, self.width, self.height),
                           self.game.character_spritesheet.getSprite(64, 256, self.width, self.height),
                           self.game.character_spritesheet.getSprite(96, 256, self.width, self.height),]
        
        rightI_animations = [self.game.character_spritesheet.getSprite(0, 32, self.width, self.height),
                           self.game.character_spritesheet.getSprite(32, 32, self.width, self.height),
                           self.game.character_spritesheet.getSprite(64, 32, self.width, self.height),
                           self.game.character_spritesheet.getSprite(96, 32, self.width, self.height),
                           self.game.character_spritesheet.getSprite(0, 32, self.width, self.height),
                           self.game.character_spritesheet.getSprite(32, 32, self.width, self.height),
                           self.game.character_spritesheet.getSprite(64, 32, self.width, self.height),
                           self.game.character_spritesheet.getSprite(96, 32, self.width, self.height),]
        
        right_animations = [self.game.character_spritesheet.getSprite(0, 288, self.width, self.height),
                           self.game.character_spritesheet.getSprite(32, 288, self.width, self.height),
                           self.game.character_spritesheet.getSprite(64, 288, self.width, self.height),
                           self.game.character_spritesheet.getSprite(96, 288, self.width, self.height),
                           self.game.character_spritesheet.getSprite(0, 320, self.width, self.height),
                           self.game.character_spritesheet.getSprite(32, 320, self.width, self.height),
                           self.game.character_spritesheet.getSprite(64, 320, self.width, self.height),
                           self.game.character_spritesheet.getSprite(96, 320, self.width, self.height),]

        if self.facing == "down":
            if self.y_change == 0:
                self.image = downI_animations[math.floor(self.animationLoop)]
                self.animationLoop += 0.1
                if self.animationLoop >= 8:
                    self.animationLoop = 1
            else:
                self.image = down_animations[math.floor(self.animationLoop)]
                self.animationLoop += 0.1
                if self.animationLoop >= 8:
                    self.animationLoop = 1

        if self.facing == "up":
            if self.y_change == 0:
                self.image = upI_animations[math.floor(self.animationLoop)]
                self.animationLoop += 0.1
                if self.animationLoop >= 8:
                    self.animationLoop = 1
            else:
                self.image = up_animations[math.floor(self.animationLoop)]
                self.animationLoop += 0.1
                if self.animationLoop >= 8:
                    self.animationLoop = 1

        if self.facing == "left":
            if self.x_change == 0:
                self.image = leftI_animations[math.floor(self.animationLoop)]
                self.animationLoop += 0.1
                if self.animationLoop >= 8:
                    self.animationLoop = 1
            else:
                self.image = left_animations[math.floor(self.animationLoop)]
                self.animationLoop += 0.1
                if self.animationLoop >= 8:
                    self.animationLoop = 1

        if self.facing == "right":
            if self.x_change == 0:
                self.image = rightI_animations[math.floor(self.animationLoop)]
                self.animationLoop += 0.1
                if self.animationLoop >= 8:
                    self.animationLoop = 1
            else:
                self.image = right_animations[math.floor(self.animationLoop)]
                self.animationLoop += 0.1
                if self.animationLoop >= 8:
                    self.animationLoop = 1

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = enemy_layer
        self.groups = self.game.all_sprites, self.game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        self.x_change = 0
        self.y_change = 0
        self.facing = random.choice(["left", "right"])
        self.animationLoop = 1
        self.movementLoop = 0
        self.maxTravel = random.randint(5, 45)

        self.image = self.game.enemy_spritesheet.getSprite(0, 0, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    
    def update(self):
        self.movement()
        self.animate()
        self.rect.x += self.x_change
        self.collideBlocks("x")
        self.rect.y += self.y_change
        self.collideBlocks("y")

        self.x_change = 0
        self.y_change = 0

    def movement(self):
        #define enemy movement
        if self.facing == "left":
            self.x_change -= enemy_speed
            self.movementLoop -= 1
            if self.movementLoop <= -self.maxTravel:
                self.facing = "right"
        
        if self.facing == "right":
            self.x_change += enemy_speed
            self.movementLoop += 1
            if self.movementLoop >= self.maxTravel:
                self.facing = "left"


    def collideBlocks(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right

        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom

    def animate(self):
        downI_animations = [self.game.enemy_spritesheet.getSprite(0, 0, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(32, 0, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(64, 0, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(96, 0, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(0, 0, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(32, 0, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(64, 0, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(96, 0, self.width, self.height)]
        
        down_animations = [self.game.enemy_spritesheet.getSprite(0, 160, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(32, 160, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(64, 160, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(96, 160, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(0, 192, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(32, 192, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(64, 192, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(96, 192, self.width, self.height),]
        
        upI_animations = [self.game.enemy_spritesheet.getSprite(0, 96, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(32, 96, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(64, 96, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(96, 96, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(0, 96, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(32, 96, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(64, 96, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(96, 96, self.width, self.height),]

        up_animations = [self.game.enemy_spritesheet.getSprite(0, 352, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(32, 352, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(64, 352, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(96, 352, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(0, 384, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(32, 384, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(64, 384, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(96, 384, self.width, self.height),]
        
        leftI_animations = [self.game.enemy_spritesheet.getSprite(0, 64, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(32, 64, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(64, 64, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(96, 64, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(0, 64, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(32, 64, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(64, 64, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(96, 64, self.width, self.height),]
        
        left_animations = [self.game.enemy_spritesheet.getSprite(0, 224, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(32, 224, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(64, 224, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(96, 224, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(0, 256, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(32, 256, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(64, 256, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(96, 256, self.width, self.height),]
        
        rightI_animations = [self.game.enemy_spritesheet.getSprite(0, 32, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(32, 32, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(64, 32, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(96, 32, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(0, 32, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(32, 32, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(64, 32, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(96, 32, self.width, self.height),]
        
        right_animations = [self.game.enemy_spritesheet.getSprite(0, 288, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(32, 288, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(64, 288, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(96, 288, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(0, 320, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(32, 320, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(64, 320, self.width, self.height),
                           self.game.enemy_spritesheet.getSprite(96, 320, self.width, self.height),]

        if self.facing == "down":
            if self.y_change == 0:
                self.image = downI_animations[math.floor(self.animationLoop)]
                self.animationLoop += 0.1
                if self.animationLoop >= 8:
                    self.animationLoop = 1
            else:
                self.image = down_animations[math.floor(self.animationLoop)]
                self.animationLoop += 0.1
                if self.animationLoop >= 8:
                    self.animationLoop = 1

        if self.facing == "up":
            if self.y_change == 0:
                self.image = upI_animations[math.floor(self.animationLoop)]
                self.animationLoop += 0.1
                if self.animationLoop >= 8:
                    self.animationLoop = 1
            else:
                self.image = up_animations[math.floor(self.animationLoop)]
                self.animationLoop += 0.1
                if self.animationLoop >= 8:
                    self.animationLoop = 1

        if self.facing == "left":
            if self.x_change == 0:
                self.image = leftI_animations[math.floor(self.animationLoop)]
                self.animationLoop += 0.1
                if self.animationLoop >= 8:
                    self.animationLoop = 1
            else:
                self.image = left_animations[math.floor(self.animationLoop)]
                self.animationLoop += 0.1
                if self.animationLoop >= 8:
                    self.animationLoop = 1

        if self.facing == "right":
            if self.x_change == 0:
                self.image = rightI_animations[math.floor(self.animationLoop)]
                self.animationLoop += 0.1
                if self.animationLoop >= 8:
                    self.animationLoop = 1
            else:
                self.image = right_animations[math.floor(self.animationLoop)]
                self.animationLoop += 0.1
                if self.animationLoop >= 8:
                    self.animationLoop = 1




class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        #assign which layer this sprite will be apart of (see config.py for layer orderings)
        self._layer = block_layer
        #assign appropriate groups this sprite belongs to
        #all_sprites & block sprites in this case
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.image = self.game.tileset32Rogues_spritesheet.getSprite(0, 64, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    
class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = ground_layer
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.tileset32Rogues_spritesheet.getSprite(0, 416, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Grass(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = ground_layer
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.tileset32Rogues_spritesheet.getSprite(32, 608, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class TopWall(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = block_layer
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.tileset32Rogues_spritesheet.getSprite(32, 64, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Obstacle01(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = block_layer
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.image = self.game.tileset32Rogues_spritesheet.getSprite(0, 736, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Obstacle02(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = block_layer
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.image = self.game.tileset32Rogues_spritesheet.getSprite(32, 800, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Button:
    def __init__(self, x, y, width, height, foreground, background, content, fontSize):
        self.font = pygame.font.Font("C:/Windows/Fonts/Arial.ttf", fontSize)
        self.content = content
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.foreground = foreground
        self.background = background

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.background)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.text = self.font.render(self.content, True, self.foreground)
        self.textRect = self.text.get_rect(center=(self.width/2, self.height/2))
        self.image.blit(self.text, self.textRect)
    
    def isPressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            return False
        return False
    
class Attack(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = player_layer
        self.groups = self.game.all_sprites, self.game.attacks
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x
        self.y = y
        self.width = TILESIZE
        self.height = TILESIZE
        self.animationLoop = 0

        self.image = self.game.attack_spritesheet.getSprite(0, 0, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.animate()
        self.collide()

    
    def collide(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemies, True)

    def animate(self):
        direction = self.game.player.facing

        down_animations = [self.game.attack_spritesheet.getSprite(0, 0, self.width, self.height),
                           self.game.attack_spritesheet.getSprite(32, 0, self.width, self.height),
                           self.game.attack_spritesheet.getSprite(64, 0, self.width, self.height),
                           self.game.attack_spritesheet.getSprite(96, 0, self.width, self.height)]
        
        up_animations = [self.game.attack_spritesheet.getSprite(0, 0, self.width, self.height),
                           self.game.attack_spritesheet.getSprite(32, 0, self.width, self.height),
                           self.game.attack_spritesheet.getSprite(64, 0, self.width, self.height),
                           self.game.attack_spritesheet.getSprite(96, 0, self.width, self.height)]
        
        left_animations = [self.game.attack_spritesheet.getSprite(0, 0, self.width, self.height),
                           self.game.attack_spritesheet.getSprite(32, 0, self.width, self.height),
                           self.game.attack_spritesheet.getSprite(64, 0, self.width, self.height),
                           self.game.attack_spritesheet.getSprite(96, 0, self.width, self.height)]
        
        right_animations = [self.game.attack_spritesheet.getSprite(0, 0, self.width, self.height),
                           self.game.attack_spritesheet.getSprite(32, 0, self.width, self.height),
                           self.game.attack_spritesheet.getSprite(64, 0, self.width, self.height),
                           self.game.attack_spritesheet.getSprite(96, 0, self.width, self.height)]

        if direction == "up":
            self.image = up_animations[math.floor(self.animationLoop)]
            self.animationLoop += 0.5
            if self.animationLoop >= 4:
                self.kill()

        if direction == "down":
            self.image = down_animations[math.floor(self.animationLoop)]
            self.animationLoop += 0.5
            if self.animationLoop >= 4:
                self.kill()

        if direction == "left":
            self.image = left_animations[math.floor(self.animationLoop)]
            self.animationLoop += 0.5
            if self.animationLoop >= 4:
                self.kill()

        if direction == "right":
            self.image = right_animations[math.floor(self.animationLoop)]
            self.animationLoop += 0.5
            if self.animationLoop >= 4:
                self.kill()