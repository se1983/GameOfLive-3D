from OpenGL.GL import *

def draw_cube(cube):
    glBegin(GL_LINES)

    [glVertex3f(*cube['vertices'][vertex]) for edge in cube['edges'] for vertex in edge]

    glEnd()