from OpenGL.raw.GL.VERSION.GL_1_1 import GL_COLOR_BUFFER_BIT

from GOL.game import GameOfLife
from Graphics.geometrics import cube
from Graphics.objects import draw_cube

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

gol = GameOfLife(4, ((1,1,1),(1,0,0),(1,2,2)))

#for point in gol.g:
#    print(point)

pygame.init()
display = (800, 800)

pygame.display.set_mode(display, GL_DOUBLEBUFFER|OPENGL)

gluPerspective(0, display[0] / display[1], 0.1, 50.0)

glTranslatef(0.0, 0.0, -5.0)

glRotatef(0, 0, 0, 0)

while True:
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            pygame.quit()
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    draw_cube(cube())



