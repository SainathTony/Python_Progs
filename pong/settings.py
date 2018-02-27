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

fol=os.path.dirname(__file__)
folder=os.path.join(fol,'images')

bgimg=os.path.join(folder,'bg.png')
mypad=os.path.join(folder,'mypad.png')
aipad=os.path.join(folder,'aipad.png')
ballimg=os.path.join(folder,'pong.png')

bgmusic=os.path.join(folder,'bgm.mp3')
hit=os.path.join(folder,'hit.ogg')
los=os.path.join(folder,'explode.ogg')

cloud=['clouds_1.png','clouds_2.png','clouds_3.png','clouds_4.png']
clouds=[]
for i in cloud:
    cld=os.path.join(folder,i)
    clouds.append(cld)
