from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

# 여기를 채우세요.

status = True
x = 400
y = 90
status_num = 0

while True:
    if status:  # 사각형
        if status_num == 0:
            while x < 800:
                clear_canvas_now()
                grass.draw_now(400, 30)
                character.draw_now(x, y)
                x = x + 2
                delay(0.01)
                if x == 798:
                    status_num = 1
        if status_num == 1:
            while y < 600:
                clear_canvas_now()
                grass.draw_now(400, 30)
                character.draw_now(x, y)
                y = y + 2
                delay(0.01)
                if y == 598:
                    status_num = 2
        if status_num == 2:
            while x >= 0:
                clear_canvas_now()
                grass.draw_now(400, 30)
                character.draw_now(x, y)
                x = x - 2
                delay(0.01)
                if x == 0:
                    status_num = 3
        if status_num == 3:
            while y >= 90:
                clear_canvas_now()
                grass.draw_now(400, 30)
                character.draw_now(x, y)
                y = y - 2
                delay(0.01)
                if y == 90:
                    x = 400
                    y = 90
                    status_num = 0
    else:  # 원
        while True:
            if x <= 400:
                clear_canvas_now()
                grass.draw_now(400, 30)
                character.draw_now(x, y)
                y = y + math.sin(y / 360 * math.pi)
                x = x + math.cos(x / 360 * math.pi)
                print(x)
                print(y)
                delay(0.01)
            if y <= 180:
                status = True
    if status:
        status = False
    else:
        status = True

close_canvas()
