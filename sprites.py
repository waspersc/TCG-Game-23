#imports libs
import pygame as pg
import random
import os

crosshair = pg.image.load("crosshair.png")
target_img = pg.image.load("target.png")

class Player(pg.sprite.Sprite):#defines the class
    def __init__(self):
       pg.sprite.Sprite.__init__(self)
       self.image = pg.transform.scale((crosshair), (70,70))
       self.rect = self.image.get_rect()#its hitbox is itself
       self.radius = 8
    def update(self):
        move = pg.mouse.get_pos()
        self.rect.center = (move)
        
        
class Target(pg.sprite.Sprite):#defines the class
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = (target_img)
        self.rect = self.image.get_rect()#its own hitbox
    def update(self):
        self.rect.center = (random.randrange(0,1500), random.randrange(0,700))
