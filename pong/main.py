import pygame as pg
from settings import *
from sprites import *
import random

class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        pg.mixer.music.load(bgmusic)
        pg.mixer.music.play()
        pg.mixer.music.set_volume(0.2)
        self.hit1=pg.mixer.Sound(hit)
        self.los1=pg.mixer.Sound(los)
        self.clouds=[]
        for i in clouds:
            img=pg.image.load(i)
            self.clouds.append(img)
        self.running=True
        self.screen=pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption('Pong!')
        self.clock=pg.time.Clock()
        self.all_sprites=pg.sprite.Group()
        self.bgimage=pg.image.load(bgimg).convert()
        pg.transform.scale(self.bgimage,(800,600))
        self.myscore=0
        self.aiscore=0
        self.bimg=pg.image.load(ballimg).convert()
        self.p1img=pg.image.load(mypad).convert()
        self.p2img=pg.image.load(aipad).convert()
        self.font=pygame.font.SysFont('calibri',50)
    def new(self):
        self.cld1=Clouds(self.clouds[1],0)
        self.cld2=Clouds(self.clouds[2],800)
        self.cld3=Clouds(self.clouds[3],800)
        self.ball=Ball(self.bimg)
        self.mypad=Pad1(self.p1img)
        self.aipad=Pad2(self.ball,self.p2img)
        self.all_sprites.add(self.ball)
        self.all_sprites.add(self.mypad)
        self.all_sprites.add(self.aipad)
        self.all_sprites.add(self.cld1)
        self.all_sprites.add(self.cld2)
        self.all_sprites.add(self.cld3)
    def run(self):
        self.new()
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    def events(self):
        global playing
        for event in pg.event.get():
            if event.type==pg.QUIT:
                self.running=False
                playing=False
    def update(self):
        self.all_sprites.update()
        hit1=pg.sprite.collide_rect(self.mypad,self.ball)
        if self.ball.rect.x<=WIDTH-25:
            if hit1:
                self.hit1.play()
                self.ball.speedx*=-1
        hit2=pg.sprite.collide_rect(self.aipad,self.ball)
        if self.ball.rect.x>=30:
            if hit2:
                self.hit1.play()
                self.ball.speedx*=-1
        if self.ball.rect.x<25:
            if not hit1:
                self.los1.play()
                self.aiscore+=1
                self.ball.rect.x=WIDTH-100
        if self.ball.rect.x>WIDTH-30:
            if not hit2:
                self.myscore+=1
                self.los1.play()
                self.ball.rect.x=100
        self.score1=self.font.render(str(self.myscore),True,WHITE)
        self.score2=self.font.render(str(self.aiscore),True,(WHITE))
    def draw(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.bgimage,(0,0))
        self.all_sprites.draw(self.screen)
        self.screen.blit(self.score1,((WIDTH//2)-20,50))
        self.screen.blit(self.score2,((WIDTH//2)+20,50))
        pg.display.flip()

playing=True
g=Game()
while playing:
    g.run()
pg.quit()
