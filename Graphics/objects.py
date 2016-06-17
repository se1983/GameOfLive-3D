from OpenGL.GL import *
from OpenGL.raw.GL.ARB.tessellation_shader import GL_TRIANGLES

from Graphics import colors


def draw_wired_cube(cube, color=(0.1,0.1,0.1), alpha=0.5):
    glBegin(GL_LINES)
    color = colors.grey + (alpha, )
    glColor4f(*color)
    [glVertex3f(*cube['vertices'][vertex] ) for edge in cube['edges'] for vertex in edge]
    glEnd()


def draw_triangled_cube(cube, alpha):
    glBegin(GL_TRIANGLES)
    color = colors.white + (alpha, )
    glColor4f(*color)

    for i, triangle in enumerate(cube['triangles']):
        glNormal3f(*cube['normals'][i])
        for vertex in triangle:
            glVertex3f(*cube['vertices'][vertex])
    glEnd()

def draw_cube(cube, alpha):
    draw_triangled_cube(cube['triangles'], alpha)
    draw_wired_cube(cube['wires'], alpha)

def draw_cube_series(cube, amount, g, alpha):
    glTranslatef(0.5 * -amount*2.1, 0.0, 0.0)
    for i in range(amount):
        if g[i]:
            draw_cube(cube, alpha)
        glTranslatef(2.1, 0.0, 0.0)
    glTranslatef(0.5 * -amount*2.1, 0.0, 0.0)

def draw_cube_area(cube, amount, g, alpha):
    glTranslatef(0.0, 0.5 * -amount * 2.1, 0.0)
    for i in range(amount):
        draw_cube_series(cube, amount, g[i], alpha)
        glTranslatef(0.0, 2.1, 0.0)
    glTranslatef(0.0, 0.5 * -amount * 2.1, 0.0)

def draw_cube_Matrix(cube, amount, g, alpha):
    glTranslatef(0.0,0.0,0.5 * -amount * 2.1)
    for i in range(amount):
        draw_cube_area(cube, amount, g[i], alpha)
        glTranslatef(0.0,0.0,2.1)
    glTranslatef(0.0,0.0,0.5 * -amount * 2.1)


def draw_coord(cube, position = (0,0,0)):
    glScale(1.0, 0.0001, 0.0001)
    draw_wired_cube(cube)
    glScale(0.0001, 1, 0.0001)
    draw_wired_cube(cube)
    glScale(0.0001, 0.0001, 1)
    draw_wired_cube(cube)
