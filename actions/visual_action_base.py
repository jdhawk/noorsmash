import pygame as pg
from pygame.math import Vector2
from random import randint

class VisualActionBase (pg.sprite.Sprite):
    
    DEFAULT_COLOR = (0, 255, 0)


    def __init__(self, height, width):
        pg.sprite.Sprite.__init__(self)
        
        self.orig_image = pg.Surface((height, width))
        self.orig_image.fill(self.DEFAULT_COLOR)
        self.rect = self.orig_image.get_rect()
        self.pos = Vector2(100,100)
        self.vel = Vector2(0,0)
        self.alpha = 255
        self.fade = False
        self.image = self.orig_image.copy()

    def update(self):
        self.pos += self.vel
        self.rect.center = self.pos
        if self.fade: 
            self.alpha = max(0, self.alpha-5)  
            self.image = self.orig_image.copy()
            self.image.fill((0, 0, 0, self.alpha), special_flags=pg.BLEND_RGBA_MULT)
            if self.alpha <= 0:
                self.kill()

    def setRandomPosition(self):
        
        width, height = pg.display.get_surface().get_size()

        self.pos = Vector2(
                randint(round(self.image.get_width() / 2), round(width - (self.image.get_width() /2))),
                randint(round(self.image.get_height() / 2), round(height - (self.image.get_height() /2))) 
            )

        
    def setRandomColor(self):
        new_color = (randint(0,255),randint(0,255),randint(0,255))

        self.orig_image.fill(new_color)
        self.image.fill(new_color)