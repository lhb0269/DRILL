import random
from pico2d import *
import game_world
import game_framework


PIXEL_PER_METER = (14.0 / 0.3)  # 14 pixel 30 cm 새의 크기 14 픽셀
FLY_SPEED_KMPH = 20.0  # Km / Hour   시간당 5km 속도
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0) # meter per minute
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)  # meter per second
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)   #pixel per second

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 /TIME_PER_ACTION
FRAMES_PER_ACTION = 14  #새의 총 애니메이션 회수 14번

class Bird:
    image = None

    def __init__(self):
        if Bird.image == None:
            Bird.image = load_image('bird100x100x14.png')
        self.x, self.y,self.velocity = random.randint(0, 1600-1), 400,1
        self.frame = 0

    def get_bb(self):
        # fill here
        return 0,0,0,0

    def draw(self):
        if self.velocity == 1:
            self.image.clip_draw(int(self.frame) * 100, 0, 100, 100, int(self.x), self.y)
        elif self.velocity == -1:
            self.image.clip_composite_draw(int(self.frame) * 100, 0, 100, 100, 2 * 3.14, 'h', int(self.x), self.y, 100, 100)
        # fill here for draw

    def update(self):
        self.frame = (self.frame+FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.x += self.velocity*FLY_SPEED_PPS*game_framework.frame_time
        if self.x >= 1600 :
            self.velocity *=-1
        elif self.x <= 0 :
            self.velocity *=-1
# class BigBall