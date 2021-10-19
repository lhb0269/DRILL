from pico2d import *
import random
# Game object class here

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()
class HERO:
    def __init__(self):
        self.image = load_image('animation_sheet.png')
        self.x = random.randint(400,600)
        self.y = 100
        self.frame = 0
    def update(self):
        self.frame = (self.frame + 1) % 8
    def draw(self):
        self.image.clip_draw(self.frame*100,100,100,100,self.x,self.y)
class BALL:
    def __init__(self):
        self.image = load_image('ball21x21.png')
        self.code = random.randint(0,1) #공 크기
        self.x = random.randint(100,500)
        self.y =  599
        self.speed = random.randint(5,10)
    def update(self):
        if self.y>=100:
            self.y -= self.speed
    def draw(self):
        if self.code == 1:
            self.image = load_image('ball21x21.png')
        if self.code == 0:
            self.image = load_image('ball41x41.png')
        self.image.draw(self.x,self.y)

# initialization code
hero = HERO()
ball1 = BALL()
ball2 = BALL()
ball3 = BALL()
ball4 = BALL()
ball5 = BALL()
ball6 = BALL()
ball7 = BALL()
ball8 = BALL()
ball9 = BALL()
ball10 = BALL()
ball11 = BALL()
ball12 = BALL()
ball13 = BALL()
ball14 = BALL()
ball15 = BALL()
ball16 = BALL()
ball17 = BALL()
ball18 = BALL()
ball19 = BALL()
ball20 = BALL()

running = True
grass = load_image('grass.png')
# game main loop code
while running:
    clear_canvas()
    hero.draw()
    ball1.draw()
    ball2 .draw()
    ball3 .draw()
    ball4 .draw()
    ball5 .draw()
    ball6 .draw()
    ball7.draw()
    ball8 .draw()
    ball9 .draw()
    ball10 .draw()
    ball11 .draw()
    ball12 .draw()
    ball13 .draw()
    ball14 .draw()
    ball15 .draw()
    ball16 .draw()
    ball17 .draw()
    ball18 .draw()
    ball19 .draw()
    ball20 .draw()
    grass.draw(400,50)

    ball1.update()
    ball2.update()
    ball3.update()
    ball4.update()
    ball5.update()
    ball6.update()
    ball7.update()
    ball8.update()
    ball9.update()
    ball10.update()
    ball11.update()
    ball12.update()
    ball13.update()
    ball14.update()
    ball15.update()
    ball16.update()
    ball17.update()
    ball18.update()
    ball19.update()
    ball20.update()
    hero.update()
    update_canvas()
    handle_events()
    delay(0.05)
# finalization code