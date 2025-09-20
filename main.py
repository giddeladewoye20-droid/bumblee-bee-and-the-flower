import random
import pgzrun

WIDTH=600
HEIGHT=600
TITLE="PAQUETA CRISPS"

bee=Actor("bee")
bee.pos=250,250
score=0
msg=""
flower=Actor("flower")
flower.pos=100,100

def draw():
    screen.clear()
    screen.blit("background", (0,0))

    bee.draw()
    flower.draw()

def update():
    if keyboard.left:
        bee.x= bee.x-2
    elif keyboard.right:
        bee.x= bee.x+2
    elif keyboard.up:
        bee.y= bee.y-2
    elif keyboard.down:
        bee.y= bee.y+2
    if bee.colliderect(flower):
        flower.pos=random.randint(0,600), random.randint(0,600)























pgzrun.go()