import os

RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
YELLOW=(255,255,0)
HEIGHT=600
WIDTH=800
FPS=60

colors=[RED,GREEN,BLUE,BLACK,WHITE,YELLOW]

fold=os.path.dirname(__file__)
folder=os.path.join(fold,'images')
bgimg=os.path.join(folder,'bg.png')
pad=os.path.join(folder,'mypad.png')
ball=os.path.join(folder,'pong.png')
stpic=os.path.join(folder,'start.png')

bgm=os.path.join(folder,'bgm.mp3')
hitsound=os.path.join(folder,'hit.wav')
