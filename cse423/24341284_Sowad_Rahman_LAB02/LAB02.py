from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random

w_width = 500
w_height = 500
diam_x = random.randint(57, 457)
diam_y = w_height
d_speed = 3
count = 0
finish = False
freeze = False
color = [random.random(), random.random(), random.random()]
plate_x = w_width // 2
plate_y = 30


def line(x1, y1, x2, y2, color):
    glColor3f(*color)
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    zoneCheck = abs(dy) > abs(dx)
    d = 2 * dy - dx
    y = y1

    if zoneCheck == True:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
        dx, dy = dy, dx

    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    d = 2 * dy - dx
    y = y1

    for x in range(int(x1), int(x2) + 1):
        if zoneCheck == True:
            glBegin(GL_POINTS)
            glVertex2f(int(y), int(x))
            glEnd()
        else:
            glBegin(GL_POINTS)
            glVertex2f(int(x), int(y))
            glEnd()

        if d > 0:
            y += 1 if y1 < y2 else -1
            d -= 2 * dx
        d += 2 * dy


def diamond(x, y):
    global color, diam_y
    line(x, y + 20, x - 15, y, color)
    line(x, y + 20, x + 15, y, color)
    line(x - 15, y, x, y - 20, color)
    line(x + 15, y, x, y - 20, color)


def plate(x, y):
    global plate_x, plate_y
    x, y = plate_x, plate_y
    line(x - 70, y, x + 70, y, [1, 0, 1])
    line(x - 70, y, x - 60, y - 20, [1, 0, 1])
    line(x + 70, y, x + 60, y - 20, [1, 0, 1])
    line(x - 60, y - 20, x + 60, y - 20, [1, 0, 1])


def restart_button():
    line(10, w_height - 30, 60, w_height - 30, [0, 0, 1])
    line(10, w_height - 30, 20, w_height - 20, [0, 0, 1])
    line(10, w_height - 30, 20, w_height - 40, [0, 0, 1])


def freeze_button():
    global freeze
    if freeze == True:
        line(w_width // 2 - 5, w_height - 20, w_width // 2 - 5, w_height - 40, [1, 1, 0])
        line(w_width // 2 - 5, w_height - 40, w_width // 2 + 20, w_height - 30, [1, 1, 0])
        line(w_width // 2 - 5, w_height - 20, w_width // 2 + 20, w_height - 30, [1, 1, 0])
    else:
        line(w_width // 2 - 5, w_height - 20, w_width // 2 - 5, w_height - 40, [1, 1, 0])
        line(w_width // 2 + 5, w_height - 20, w_width // 2 + 5, w_height - 40, [1, 1, 0])


def exit_button():
    line(w_width - 30, w_height - 20, w_width - 10, w_height - 40, [1, 0, 0])
    line(w_width - 30, w_height - 40, w_width - 10, w_height - 20, [1, 0, 0])


def mouse_click(button, state, x, y):
    global finish, count, d_speed, diam_x, diam_y, freeze, color
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        y = w_height - y
        if (x >= (w_width - 50) and x <= (w_width - 10) and y >= (w_height - 50) and y <= (w_height - 10)):
            print("Thank you for Playing ")
            print(f"Total Collected Diamonds: {count}")
            glutLeaveMainLoop()


        elif (x >= (w_width // 2 - 20) and x <= (w_width // 2 + 20) and y >= (w_height - 50) and y <= (w_height - 10)):
            if finish == False:
                freeze = not freeze

        elif (x >= 10 and x <= 60 and y >= (w_height - 50) and y <= (w_height - 10)):
            print("Restarting Game")

            finish = False
            count = 0
            d_speed = 2
            diam_x = random.randint(50, w_width - 50)
            diam_y = w_height - 50
            freeze = False
            color = [random.random(), random.random(), random.random()]


def special_keys(key, x, y):
    global plate_x
    if freeze == False:
        step = 10
        if finish == False:
            if key == GLUT_KEY_RIGHT:
                plate_x = min(plate_x + step, w_width - 70)
            elif key == GLUT_KEY_LEFT:
                plate_x = max(plate_x - step, 70)


def position_update(val):
    global diam_x, diam_y, count, d_speed, finish, color, plate_x, plate_y
    if freeze == False and finish == False:
        diam_y -= d_speed
        if diam_y < 0:
            finish = True
            print("Game Over. Total Collected: ", count)

        if plate_x - 70 <= diam_x and diam_x <= plate_x + 70 and plate_y <= diam_y and diam_y <= plate_y + 20:
            count += 1
            d_speed += 0.2
            print("Diamonds Collected:", count)
            diam_x = random.randint(57, 457)
            diam_y = w_height
            color = [random.random(), random.random(), random.random()]

    glutPostRedisplay()
    glutTimerFunc(30, position_update, 0)


def show_screen():
    glClear(GL_COLOR_BUFFER_BIT)
    restart_button()
    freeze_button()
    exit_button()
    diamond(diam_x, diam_y)
    plate(plate_x, plate_y)
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(500, 500)
glutCreateWindow(b"Collect Diamonds")
glOrtho(0, 500, 0, 500, -1, 1)
glClearColor(0, 0, 0, 1)

glutDisplayFunc(show_screen)
glutSpecialFunc(special_keys)
glutMouseFunc(mouse_click)
glutIdleFunc(show_screen)
glutDisplayFunc(show_screen)

glutSpecialFunc(special_keys)
glutIdleFunc(show_screen)
glutTimerFunc(100, position_update, 0)

glutMainLoop()
