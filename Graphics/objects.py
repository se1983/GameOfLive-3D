from OpenGL.GL import *
from OpenGL.raw.GL.ARB.tessellation_shader import GL_TRIANGLES


def draw_wired_cube(cube):
    glBegin(GL_LINES)
    [glVertex3f(*cube['vertices'][vertex]) for edge in cube['edges'] for vertex in edge]
    glEnd()

def draw_triangled_cube(cube):
    glBegin(GL_TRIANGLES)
    for triangle in cube['triangles']:
        for vertex in triangle:
            glVertex3f(*cube['vertices'][vertex])
    glEnd()

def draw_cube(cube):
    draw_wired_cube(cube)
