from pico2d import *
from random import randint
KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def init_hand():
    global object_x
    global object_y
    global objectinit
    if objectinit == False:
        object_x = randint(0, 1280)
        object_y = randint(0, 1024)
        objectinit = True
    handobject.draw(object_x,object_y)
def handle_events():
   global running
   events = get_events()
   for event in events:
       if event.type == SDL_QUIT:
           running = False
       elif event.type == SDL_KEYDOWN:
           if event.key == SDLK_ESCAPE:
               running = False
def charcter_move():
    global x,y
    global object_x
    global object_y
    global objectinit
    global move_code
    if(x<object_x):
        x+=1
        move_code=0
    if (x > object_x):
        x -= 1
        move_code=1
    if (y < object_y):
        y += 1
    if (y > object_y):
        y -= 1
    if(x==object_x and y==object_y):
        objectinit=False
def animation():
    global move_code
    if move_code==0:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    if move_code==1:
        character.clip_draw(frame * 100, 0 * 1, 100, 100, x, y)
open_canvas(KPU_WIDTH,KPU_HEIGHT)
# fill here
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
handobject = load_image('hand_arrow.png')
object_x = randint(0, 1280)
object_y = randint(0, 1024)


running = True
objectinit = False

x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
hide_cursor()
move_code =0#방향 오른쪽방향 0 왼쪽방향 1

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    animation()
    init_hand()
    update_canvas()
    frame = (frame + 1) % 8
    charcter_move()
    handle_events()

close_canvas()




