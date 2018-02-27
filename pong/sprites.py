import pygame
from settings import *
import random

class Ball(pygame.sprite.Sprite):
    def __init__(self,bimg):
        pygame.sprite.Sprite.__init__(self)
        #self.image=pygame.Surface((15,15))
        #self.image.fill(BLACK)
        #self.cir=pygame.draw.circle(self.image,YELLOW,((15//2),(15//2)),int(15/2))
        self.image=bimg
        self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()
        self.rect.x=100
        self.rect.y=300
        self.speedx=5
        self.speedy=5
    def update(self):
        if self.rect.y>=HEIGHT-15:
            self.speedy*=-1
        if self.rect.y<=0:
            self.speedy*=-1
        if self.rect.x>=WIDTH-15:
            self.speedx*=-1
        if self.rect.x<=0:
            self.speedx*=-1
        self.rect.x+=self.speedx
        self.rect.y+=self.speedy
        
class Pad1(pygame.sprite.Sprite):
    def __init__(self,p1img):
        pygame.sprite.Sprite.__init__(self)
        #self.image=pygame.Surface((10,80))
        #self.image.fill(GREEN)
        self.image=p1img
        self.rect=self.image.get_rect()
        self.speed=4
        self.rect.x=10
        self.rect.y=300
    def update(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            self.rect.y+=self.speed
            if self.rect.y>=HEIGHT-80:
                self.rect.y=HEIGHT-80
        if keys[pygame.K_UP]:
            self.rect.y-=self.speed
            if self.rect.y<=0:
                self.rect.y=0

class Pad2(pygame.sprite.Sprite):
    def __init__(self,ball,p2img):
        pygame.sprite.Sprite.__init__(self)
        #self.image=pygame.Surface((10,80))
        #self.image.fill(BLUE)
        self.image=p2img
        self.rect=self.image.get_rect()
        self.speed=5
        self.rect.x=WIDTH-20
        self.rect.y=300
        self.ball=ball
    def update(self):
        if self.ball.rect.x>=500:
            if self.ball.rect.y+10>=self.rect.y+40:
                self.rect.y+=self.speed
                if self.rect.y>=HEIGHT-80:
                    self.rect.y=HEIGHT-80
            if self.ball.rect.y+10<=self.rect.y+40:
                self.rect.y-=self.speed
                if self.rect.y<=0:
                    self.rect.y=0



class Clouds(pygame.sprite.Sprite):
    def __init__(self,cld,x):
        pygame.sprite.Sprite.__init__(self)
        self.image=cld
        self.rect=self.image.get_rect()
        self.speed=2
        self.rect.x=x
        self.rect.y=0

    def update(self):
        self.rect.x-=self.speed
        if self.rect.x<=-800:
            self.rect.x=800
        




            


        
