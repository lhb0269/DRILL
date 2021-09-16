from pico2d import *
from math import *


x,y=400,90
r=200
move_code=0
 
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

while 1:
    while move_code!=5:
        if move_code==0:
            x+=5
            if x>=800:
                move_code=1
        if move_code==1:
            y+=5
            if y>=600:
                move_code=2
        if move_code==2:
            x-=5
            if x<=0:
                move_code=3
        if move_code==3:
            y-=5
            if y<=90:
                move_code=4
        if move_code==4:
            if x<400:
                x+=5
                if x>=400:
                    move_code=5
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        delay(0.01)
    while move_code==5:
        for i in range(100):
            angle = i*2*math.pi/100
            x=math.cos(angle)*400+400
            y=math.sin(angle)*300+300
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            delay(0.01)
        move_code=0
close_canvas()
