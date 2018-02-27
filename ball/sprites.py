import pygame as pg
import random
from settings import *

class Bubble(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.image=pg.Surface((40,10))
        self.image.fill((random.randint(0,250),random.randint(0,250),random.randint(0,250)))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

class Pad(pg.sprite.Sprite):
    def __init__(self,pad):
        pg.sprite.Sprite.__init__(self)
        #self.image=pg.Surface((80,20))
        self.image=pad
        #self.image.fill(BLUE)
        self.rect=self.image.get_rect()
        self.rect.x=400
        self.rect.y=HEIGHT-30
        self.speed=5

    def update(self):
        keys=pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.rect.x-=self.speed
            if self.rect.x<=0:
                self.rect.x=0
        if keys[pg.K_RIGHT]:
            self.rect.x+=self.speed
            if self.rect.x+80>=800:
                self.rect.x=720

class Ball(pg.sprite.Sprite):
    def __init__(self,pad,ball):
        self.run=False
        self.pad=pad
        pg.sprite.Sprite.__init__(self)
        #self.image=pg.Surface((20,20))
        self.image=ball
        #self.image.fill(BLACK)
        #pg.draw.circle(self.image,GREEN,(10,10),10,0)
        self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()
        self.rect.x=self.pad.rect.x+40
        self.rect.y=self.pad.rect.y-20
        self.speedx=5
        self.speedy=5

    def update(self):
        keys=pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            self.run=True
        if self.run:
            self.rect.x+=self.speedx
            self.rect.y-=self.speedy
            if self.rect.x<=0:
                self.speedx*=-1
            if self.rect.x+20>=800:
                self.speedx*=-1
            if self.rect.y<=0:
                self.speedy*=-1
            if self.rect.y>=HEIGHT:
                self.run=False
                self.rect.x=self.pad.rect.x+40
                self.rect.y=self.pad.rect.y-20
        else:
            self.rect.x=self.pad.rect.x+40
            self.rect.y=self.pad.rect.y-20

class Live(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image=pg.Surface((200,30))
        self.image.fill(RED)
        self.rect=self.image.get_rect()
        self.rect.x=10
        self.rect.y=10
        
class Fill(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image=pg.Surface((0,30))
        self.image.fill(GREEN)
        self.rect=self.image.get_rect()
        self.rect.x=10
        self.rect.y=10
        self.x=200

    def update(self,x):
        self.x-=x
        self.image=pg.Surface((self.x,30))
        self.image.fill(GREEN)


        
