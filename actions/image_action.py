import pygame as pg
from pygame.math import Vector2
from actions.visual_action_base import VisualActionBase


class ImageAction (VisualActionBase):

    def __init__(self, imagePath):
        pg.sprite.Sprite.__init__(self)
        
        print ("Loading: " + imagePath)
        self.orig_image = pg.image.load(imagePath)
        self.orig_image.set_colorkey((255,255,255))
        self.rect = self.orig_image.get_rect()
        self.pos = Vector2(100,100)
        self.vel = Vector2(0,0)
        self.alpha = 255
        self.fade = False
        self.image = self.orig_image.copy()


    def setRandomColor(self):
        return