from OpenGL.GL import *

def draw_cube(cube):
    glBegin(GL_LINES)
    for edge in cube['edges']:
        for vertex in edge:
            glVertex3f(*cube['vertices'][vertex])
    glEnd