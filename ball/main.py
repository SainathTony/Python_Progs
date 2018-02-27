import pygame as pg
from settings import *
from sprites import *
import random
import time

pg.init()
pg.mixer.init()

class Game:
    def __init__(self):
        self.running=True
        self.clock=pg.time.Clock()
        self.screen=pg.display.set_mode((800,600))
        pg.display.set_caption('Bubble Shoot!')
        self.bubble_list=pg.sprite.Group()
        self.all_sprites=pg.sprite.Group()
        self.ballpic=pg.image.load(ball)
        self.bgp=pg.image.load(bgimg)
        self.mypad=pg.image.load(pad)
        self.startpic=pg.image.load(stpic)
        self.bgm=pg.mixer.music.load(bgm)
        self.hitsnd=pg.mixer.Sound(hitsound)
        pg.mixer.music.play(loops=-1)
        pg.mixer.music.set_volume(0.4)
    def new(self):
        x=10
        y=50
        for i in range(100):
            self.bubble=Bubble(x,y)
            self.bubble_list.add(self.bubble)
            x+=50
            if x>760:
                x=10
                y+=20
        self.pad=Pad(self.mypad)
        self.ball=Ball(self.pad,self.ballpic)
        self.live=Live()
        self.fill=Fill()
        self.all_sprites.add(self.pad)
        self.all_sprites.add(self.ball)
        self.all_sprites.add(self.live)
    def run(self):
        self.start()
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
        hits=pg.sprite.spritecollide(self.ball,self.bubble_list,True)
        if hits:
            self.hitsnd.play()
            self.ball.speedy*=-1

        hit=pg.sprite.collide_rect(self.pad,self.ball)
        if hit and self.ball.rect.y<=HEIGHT-15:
            self.ball.speedy*=-1

        if self.ball.rect.y==HEIGHT-5:
            self.fill.update(50)
            if self.fill.x<=0:
                self.showgameover()

    def draw_text(self,text,color,size,x,y):
        font2=pg.font.SysFont('calibri',size)
        name=font2.render(text,True,(color))
        self.screen.blit(name,(x,y))
        
    def showgameover(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.bgp,(0,0))
        self.draw_text("GAME OVER",WHITE,50,300,200)
        self.draw_text("Press any key to restart",WHITE,20,300,500)
        pg.display.flip()
        time.sleep(2)
        self.waiting=True
        while self.waiting:
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    self.running=False
                    playing=False
                    pg.quit()
                if event.type==pg.KEYUP:
                    self.waiting=False
        self.pad.kill()
        self.ball.kill()
        self.bubble_list=pg.sprite.Group()
        self.all_sprites=pg.sprite.Group()
        self.new()

    def start(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.startpic,(0,0))
        self.draw_text("Press any key to restart",WHITE,50,150,550)
        pg.display.flip()
        self.waiting=True
        while self.waiting:
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    self.running=False
                    playing=False
                    pg.quit()
                if event.type==pg.KEYUP:
                    self.waiting=False
                    return
    
    def draw(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.bgp,(0,0))
        self.all_sprites.draw(self.screen)
        self.bubble_list.draw(self.screen)
        self.screen.blit(self.fill.image,(10,10))
        pg.display.flip()

    
playing=True
g=Game()
while playing:
    g.run()
pg.quit()
