from OpenGL.GL import *
from OpenGL.raw.GL.ARB.tessellation_shader import GL_TRIANGLES



def draw_wired_cube(cube):
    glBegin(GL_LINES)
    glColor3f(0,1,0)
    [glVertex3f(*cube['vertices'][vertex]) for edge in cube['edges'] for vertex in edge]
    glEnd()

def draw_triangled_cube(cube):
    glBegin(GL_TRIANGLES)
    glColor3f(0.3, 0.3, 0.3)
    for i, triangle in enumerate(cube['triangles']):
        for vertex in triangle:
            glNormal3f(*cube['normals'][i])
            glVertex3f(*cube['vertices'][vertex])
    glEnd()

def draw_cube(cube):
    draw_triangled_cube(cube['triangles'])
    draw_wired_cube(cube['wires'])

def draw_cube_series(cube, amount = 2):
    for i in range(amount):
        draw_cube(cube)
        glTranslatef(2.1, 0.0, 0.0)
    glTranslatef(-amount*2.1, 0.0, 0.0)

def draw_cube_area(cube, amount=2):
    for i in range(amount):
        draw_cube_series(cube, amount)
        glTranslatef(0.0, 2.1, 0.0)
    glTranslatef(0.0, -amount * 2.1, 0.0)

def draw_cube_cube(cube, amount=2):
    for i in range(amount):
        draw_cube_area(cube, amount)
        glTranslatef(0.0,0.0,2.1)
    glTranslatef(0.0,0.0,-amount * 2.1)




