import pygame
from config import *
import math
import random

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

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill("#9cabd0")

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.movement()
        self.rect.x += self.x_change
        self.rect.y += self.y_change

        #calculate the change in velocity
        self.x_change = 0
        self.y_change = 0
    
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x_change -= player_speed
            self.facing = 'left'
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x_change += player_speed
            self.facing = 'right'
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y_change += player_speed
            self.facing = 'down'
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y_change -= player_speed
            self.facing = 'up'

class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = block_layer
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill("#7DDEA8")

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        