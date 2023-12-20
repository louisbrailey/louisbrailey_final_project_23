# This file was created by: Carlos Gomez and Louis Brailey 

import pygame as pg

from pygame.sprite import Sprite

from pygame.math import Vector2 as vec

import os

from settings import *
 
# setup asset folders here - images sounds etc.

game_folder = os.path.dirname(__file__)

img_folder = os.path.join(game_folder, 'images')

snd_folder = os.path.join(game_folder, 'sounds')
 
class Player(Sprite):

    def __init__(self, game):

        super().__init__()

        self.game = game

        self.image = pg.image.load(os.path.join(img_folder, 'theBigBell.png')).convert()

        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()

        self.rect.center = (0, 0)

        self.pos = vec(WIDTH / 2, HEIGHT / 2)

        self.vel = vec(0, 0)

        self.acc = vec(0, 0)

        self.hitpoints = 100

    
            

    def controls(self):

        keys = pg.key.get_pressed()

        self.acc.x = 0  # Reset acceleration each frame

        if keys[pg.K_a]:

            self.acc.x = -5

        if keys[pg.K_d]:
            if self.rect.x < WIDTH - (WIDTH/4):
                self.acc.x = 5

        if keys[pg.K_SPACE]:

            self.jump()
 
    def jump(self):

        hits = pg.sprite.spritecollide(self, self.game.all_platforms, False)

        ghits = pg.sprite.collide_rect(self, self.game.ground)

        if hits or ghits:

            print("i can jump")

            self.vel.y = -PLAYER_JUMP
 
    def update(self):

        self.acc = vec(0, PLAYER_GRAV)
        
        self.controls()
        self.acc.x += self.vel.x * -PLAYER_FRIC
        self.vel += self.acc

        self.pos += self.vel + 0.5 * self.acc

        self.rect.midbottom = self.pos

    
 
class PlatformBase(Sprite):

    def __init__(self, x, y, w, h, category):

        super().__init__()

        self.image = pg.Surface((w, h))

        self.rect = self.image.get_rect()

        self.rect.x = x

        self.rect.y = y

        self.category = category

        self.speed = 0

        if self.category == "moving":

            self.speed = 5
 
    def update(self):

        if self.category == "moving":

            self.rect.x += self.speed

            if self.rect.x + self.rect.w > WIDTH or self.rect.x < 0:

                self.speed = -self.speed
 
class Platform(PlatformBase):

    def __init__(self, x, y, w, h, category):

        super().__init__(x, y, w, h, category)

        self.image = pg.image.load(os.path.join(img_folder, 'Rock.png')).convert()
 
class Fplatform(PlatformBase):

    def __init__(self, x, y, w, h, category):

        super().__init__(x, y, w, h, category)

        self.image.fill(BROWN)
 
class FinishLine(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface((WIDTH, 5))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Mob(Sprite):
    def __init__(self, x, y, w, h, kind):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.kind = kind
        self.pos = vec(WIDTH/2, HEIGHT/2)
        
        
        # makes the mobs move

        self.mob = 'moving'
        if self.mob == "moving":

            self.speed = 5
    def update(self):
        if self.mob == "moving":

            self.rect.x += self.speed

            

            if self.rect.x + self.rect.w > WIDTH or self.rect.x < 0:

                self.speed = -self.speed
    
        
        pass

 
# Additional improvements:

# - Used constants for keys in Player class.

# - Moved common functionalities of Platform and Fplatform to a base class.
