from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

h = 500
w = 500
rain = []  # brishtir list
light = False
position = 0  # rotation handle korbo 1
background = [0.0, 0.0, 0.0]  # kalo
final_cng = [0.0, 0.0, 0.0]  # je color e bg nibo
speed = 0.5


def draw_line(x1, y1, x2, y2):
    glLineWidth(5.0)
    glBegin(GL_LINES)
    if light == False:
        glColor3f(1.0, 0.4, 0.0)  # night house = purple
    elif light == True:
        glColor3f(1.0, 0.0, 0.0)  # day house = red
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()


def draw_rain():
    glLineWidth(2.0)
    glBegin(GL_LINES)  # brishti koto mota hobe
    if light == False:
        glColor3f(1.0, 1.0, 1.0)  # night rain = white
    elif light == True:
        glColor3f(0.0, 0.0, 0.0)  # day rain = black
    for x, y in rain:
        glVertex2f(x - position, y)  # rotation handling 2
        glVertex2f(x + position, y - 15)  # rotation handling 3,brishtir fotar length handling
    glEnd()


def generation():
    global rain
    x = random.randint(150, 450)
    y = 500
    rain.append((x, y))


def animation():
    global rain
    rain1 = []
    for x, y in rain:
        y -= 1
        if y >= 100:
            rain1.append((x, y))

    rain = rain1


def change_background():
    global background, final_cng, speed

    for i in range(3):
        if background[i] < final_cng[i]:
            background[i] += speed
        elif background[i] > final_cng[i]:
            background[i] -= speed


def iterate():
    glViewport(0, 0, w,
               h)  # kothai akbo screen er, jemon 0,0 mane ekdom left bottom e, ar width r height define kore disi ekdom upore
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()  # identity matrix e reload mare
    glOrtho(0.0, w, 0.0, h, 0.0, 1.0)  # clip kore
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClearColor(*background, 0.0)  # shob black kore dei


def showScreen():
    # shob functions call disi
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    draw_rain()
    animation()
    generation()
    change_background()

    # Updated coordinates (twice the size)
    draw_line(200, 200, 400, 200)
    draw_line(200, 200, 200, 350)
    draw_line(200, 350, 400, 350)
    draw_line(400, 200, 400, 350)
    draw_line(200, 350, 300, 400)
    draw_line(400, 350, 300, 400)
    draw_line(240, 200, 240, 275)
    draw_line(290, 200, 290, 275)
    draw_line(240, 275, 290, 275)
    draw_line(330, 250, 330, 290)
    draw_line(330, 290, 370, 290)
    draw_line(370, 290, 370, 250)
    draw_line(370, 250, 330, 250)

    glutSwapBuffers()  # double buffering ,reduce flickering


# glutSwapBuffers() is a function in the GLUT (OpenGL Utility Toolkit) library that is
#  commonly used in OpenGL programs to implement double buffering. Double buffering is a technique
#  used to reduce flickering in computer graphics.

def keyboardListener(key, x, y):
    global final_cng, light

    if key == b'd':
        if light == False:
            final_cng = [1.0, 1.0, 1.0]  # je color e jaite chai, white (din)
            light = True
    elif key == b'n':
        if light == True:
            final_cng = [0.0, 0.0, 0.0]  # black (night)
            light = False
    glutPostRedisplay()


def specialKeyListener(key, x, y):
    global position

    if key == GLUT_KEY_RIGHT:
        position += 0.1  # brishti rotation handling 4
    elif key == GLUT_KEY_LEFT:
        position -= 0.1  # brishti rotation handling 5
    glutPostRedisplay()  # ami jokhon brishtir angle, or kichur speed barai ba komai, i need to call the screen
    # and draw everything again


# glutPostRedisplay() is a function in the GLUT (OpenGL Utility Toolkit) library that is used
# to mark the current window as needing a redisplay. In other words, it tells the GLUT system that the window's
# contents have changed and need to be redrawn. This function is often used in the display callback function to request
#  that the window be redrawn in response to changes in the scene.

# Here's how it works:

# When you make changes to the OpenGL scene or graphics in your application, you need to indicate that
# the contents of the current window have been modified and should be updated.

# By calling glutPostRedisplay(), you inform GLUT that the window associated with the current
#  rendering context needs to be redisplayed.

# The GLUT main loop (glutMainLoop()) periodically checks if the window needs to be redisplayed.
# When it detects that a window is marked for redisplay (usually as a result of glutPostRedisplay() being called),
# it invokes the display callback function you've registered (e.g., glutDisplayFunc()), allowing you to redraw the scene.


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 1000)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Task 1")
glutDisplayFunc(showScreen)
glutSpecialFunc(specialKeyListener)
glutKeyboardFunc(keyboardListener)
glutIdleFunc(showScreen)
# function will be repeatedly called by GLUT during idle time, allowing you to continuously
#  update the rendering of your scene. This is essential for animations and real-time graphics.
glutMainLoop()




