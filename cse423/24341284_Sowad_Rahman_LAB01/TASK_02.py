from OpenGL.GL import *
from OpenGL.GLUT import *
import random

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
glutInitWindowSize(500, 500)
glutCreateWindow(b"Task 2")
h, w = 500, 500
pointlist = []
pointSpeed = .000001
freeze = False
blink = False


# Function to generate random points
def generate_point(x, y):
    color = (random.random(), random.random(), random.random())
    background = (0.0, 0.0, 0.0)
    if random.random() < 0.5:
        direction_x = 1
    else:
        direction_x = -1

    if random.random() < 0.5:
        direction_y = 1
    else:
        direction_y = -1

    pointlist.append((x, y, direction_x, direction_y, color, background))


# Function to handle mouse events
def mouseListener(button, state, x, y):
    global pointSpeed, freeze, blink
    if freeze == False:
        if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
            x = (x / w - 0.5) * 2
            y = (0.5 - y / h) * 2
            generate_point(x, y)
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            blink = True


def specialKeyListener(key, x, y):
    global pointSpeed, freeze
    if key == GLUT_KEY_UP:
        pointSpeed *= 2
    elif key == GLUT_KEY_DOWN:
        pointSpeed /= 2


def keyboard(key, x, y):
    global speed, freeze
    if key == b' ':
        freeze = not freeze


def draw_points():
    glPointSize(5)
    glBegin(GL_POINTS)
    for x, y, a, b, color, sc in pointlist:
        glColor3f(*color)
        glVertex2f(x, y)
    glEnd()


def update_points():
    global pointSpeed, freeze
    if freeze == False:
        if blink == False:
            for i in range(len(pointlist)):
                x, y, dx, dy, c, sc = pointlist[i]
                x += dx * pointSpeed
                y += dy * pointSpeed
                pointlist[i] = (x, y, dx, dy, c, sc)
        else:
            for i in range(len(pointlist)):
                x, y, dx, dy, c, sc = pointlist[i]

                x += dx * pointSpeed
                y += dy * pointSpeed
                pointlist[i] = (x, y, dx, dy, sc, c)


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_points()
    glutSwapBuffers()
    update_points()
    glutPostRedisplay()


glClearColor(0.0, 0.0, 0.0, 0.0)
glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)
glutDisplayFunc(display)
glutMouseFunc(mouseListener)
glutSpecialFunc(specialKeyListener)
glutKeyboardFunc(keyboard)
glutMainLoop()