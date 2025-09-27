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
gameover=False

def timer():
    global gameover
    gameover=True
clock.schedule(timer,10)

def draw():
    screen.clear()
    if gameover==False:
        screen.blit("background", (0,0))
        bee.draw()
        flower.draw()
        screen.draw.text(msg,center=(250,250),fontsize=30,color="purple")
    else:
        screen.fill("black")
        screen.draw.text("GAMEOVER\nYour total points are"+ str (score),center=(250,250),fontsize=60,color="yellow")

def update():
    global msg
    global score
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
        score= score + 1
        msg="You have hit the Flower!You now have " + str (score)+"points"

   






















pgzrun.go()