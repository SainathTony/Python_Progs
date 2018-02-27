import pygame
import time
import os

pygame.init()
pygame.mixer.init()

RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
HEIGHT=600
WIDTH=800
FPS=60

fol=os.path.dirname(__file__)
folder=os.path.join(fol,'images')

pad1y=300
pad1x=10
startimg=os.path.join(folder,'start.png')
aipad=os.path.join(folder,'aipad.png')
mypad=os.path.join(folder,'mypad.png')
ballimg=os.path.join(folder,'pong.png')

s=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Ball JUMP!')
clock=pygame.time.Clock()

font=pygame.font.SysFont('calibri',50)

def draw_text(text,color,size,x,y):
    font2=pygame.font.SysFont('calibri',size)
    name=font2.render(text,True,(color))
    s.blit(name,(x,y))

def gameover_screen(text):
    img=pygame.image.load(startimg).convert()
    s.blit(img,(0,0))
    draw_text('Game Over',WHITE,50,(WIDTH//2)-40,100)
    draw_text(text,WHITE,50,WIDTH//2,HEIGHT//2)
    pygame.display.flip()
    waiting=True
    while waiting:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                crashed=True
                waiting=False
            if event.type==pygame.KEYUP:
                waiting=False

def show_start():
    img=pygame.image.load(startimg).convert()
    s.blit(img,(0,0))
    draw_text('ping pong!',WHITE,60,280,50)
    draw_text('press any key to begin',WHITE,20,230,HEIGHT*3/2)
    pygame.display.flip()
    waiting=True
    while waiting:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                crashed=True
                waiting=False
            if event.type==pygame.KEYUP:
                waiting=False


bck=pygame.Surface((WIDTH,HEIGHT))
bck.fill(WHITE)

border=pygame.Surface((WIDTH-20,HEIGHT-20))
border.fill(BLACK)

class ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(ballimg).convert()
        #self.cir=pygame.draw.circle(self.image,GREEN,((15//2),(15//2)),int(15/2))
        #self.image=self.cir.convert()
        self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()
        self.speedx=5
        self.speedy=5
        self.rect.x=400
        self.rect.y=100
        self.myscore=0
        self.aiscore=0
        self.run=True
    def update(self):
        if(self.rect.x>=WIDTH-20):
            self.rect.x=50
            self.myscore+=1
            self.speedx*=-1
            #self.run=False
        if(self.rect.x<=10):
            self.speedx*-1
            self.rect.x=WIDTH-50
            self.aiscore+=1
        if(self.rect.y>=HEIGHT-20):
            self.speedy*=-1
        if(self.rect.y<=10):
            self.speedy*=-1
        if self.run:
            self.rect.x+=self.speedx
            self.rect.y+=self.speedy
        for event in pygame.event.get():
            if event.type==pygame.KEYUP:
                    if event.key==pygame.K_SPACE:
                        self.run=True

class pad(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(aipad).convert()
        self.rect=self.image.get_rect()
        self.speedy=4
        self.rect.x=10
        self.rect.y=300
    def update(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            self.rect.y+=self.speedy
            if(self.rect.y>=HEIGHT-80):
                self.rect.y=HEIGHT-80
        if keys[pygame.K_UP]:
            self.rect.y-=self.speedy
            if(self.rect.y<=10):
                self.rect.y=10

class pad2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(mypad).convert()
        self.rect=self.image.get_rect()
        self.speedy=4
        self.rect.x=WIDTH-30
        self.rect.y=300
    def update(self):
        if pad2.rect.y>=HEIGHT-80:
            pad2.rect.y=HEIGHT-80
        if pad2.rect.y<=10:
            pad2.rect.y=10

all_sprites=pygame.sprite.Group()
pad1=pad()
pad2=pad2()
ball=ball()
all_sprites.add(ball)
all_sprites.add(pad1)
all_sprites.add(pad2)


crashed=False
gameover=True
x=300
y=(HEIGHT//5)
xspeed=5
yspeed=5
padx=(WIDTH//5)
direction='up'
bg=os.path.join(folder,'bg.png')
bgimage=pygame.image.load(bg).convert()
pad2speed=5
while not crashed:
    clock.tick(FPS)
    if gameover:
        show_start()
        gameover=False
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            crashed =True

    hit1=pygame.sprite.collide_rect(pad1,ball)
    if ball.rect.x>=25:
        if hit1:
            ball.speedx*=-1
    if ball.rect.x>=300:
        if ball.rect.y>=pad2.rect.y and ball.rect.y<=pad2.rect.y+50:
            pad2.rect.y=pad2.rect.y
        else:
            if ball.rect.y>=pad2.rect.y+45:
                pad2.rect.y+=pad2speed
            if ball.rect.y<=pad2.rect.y-5:
                pad2.rect.y-=pad2speed
                
        
    if ball.rect.y<=pad2.rect.y+75 and ball.rect.y+5>=pad2.rect.y and ball.rect.x>=WIDTH-30 and ball.rect.x<=WIDTH-25:
        ball.speedx*=-1
    score1=font.render(str(ball.myscore),True,WHITE)
    score2=font.render(str(ball.aiscore),True,(WHITE))        
        
    pad1x=pad1.rect.x
    pad1y=pad1.rect.y
    s.blit(bgimage,(0,0))
    s.blit(ball.image,(ball.rect.x,ball.rect.y))
    s.blit(pad1.image,(pad1.rect.x,pad1.rect.y))
    s.blit(pad2.image,(pad2.rect.x,pad2.rect.y))
    s.blit(score1,(350,50))
    s.blit(score2,(420,50))
    if ball.myscore>=10:
        gameover_screen('You Win')
        gameover=True
        ball.myscore=0
        ball.aiscore=0
        
    if ball.aiscore>=10:
        gameover_screen('You Loss')
        gameover=True
        ball.myscore=0
        ball.aiscore=0
        
    all_sprites.update()
    pygame.display.flip()
pygame.quit()
