from pico2d import *
import math


open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def render_frame(x, y):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    delay(0.01)
    
def run_circle():
    print("circle")

    # 일단 그림을 그리자
    cx, cy, r = 400, 300, 210
    for deg in range(-90, 270, 3):
        x = cx + r * math.cos(math.radians(deg))
        y = cy + r * math.sin(math.radians(deg))
        render_frame(x,y)

def run_ractangle():
    print("ractangle")

    for x in range(400, 750+1, 10):
        render_frame(x,90)

    for y in range(90, 550+1, 10):
        render_frame(x,y)
    
    for x in range(750, 50-1, -10):
        render_frame(x,y)

    for y in range(550, 90-1, -10):
        render_frame(x,y)

    for x in range(50, 400+1, 10):
        render_frame(x,y)

while True:
    run_circle()
    run_ractangle()

close_canvas()
