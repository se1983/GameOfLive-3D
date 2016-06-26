
from OpenGL.GL import *
from OpenGL.raw.GL.ARB.tessellation_shader import GL_TRIANGLES

from Graphics import colors, geometrics


class Cube():

    def __init__(self, position):
        self.cube = geometrics.cube()
        self.alpha = 0.5
        self.position = position

    def draw(self, alpha=None):
        if not alpha:
            alpha = self.alpha

        # We translate 2.1 for each cube
        # so the cube has exactly the size of 2 we get a gap of 0.1
        # We do only halfe, because we want the center more in the middle of
        # the playground.
        trans = [0.5 * 2.1 * n for n in self.position]
        glTranslatef(*trans)
        self.__draw_wired_cube(colors.grey, alpha)
        self.__draw_triangled_cube(colors.green, alpha)
        # The translation back needs the negative values
        trans = [-n for n in trans]
        glTranslatef(*trans)

    def blend_in(self):
        pass

    def blend_in(self):
        pass

    def __draw_wired_cube(self, color, alpha):
        cube = geometrics.wired_cube()
        glBegin(GL_LINES)
        color += (alpha, )
        glColor4f(*color)
        [glVertex3f(*cube['vertices'][vertex]) for edge in cube['edges'] for vertex in edge]
        glEnd()

    def __draw_triangled_cube(self, color, alpha):
        cube = geometrics.triangled_cube()
        glBegin(GL_TRIANGLES)
        color += (alpha, )
        glColor4f(*color)

        for i, triangle in enumerate(cube['triangles']):
            glNormal3f(*cube['normals'][i])
            for vertex in triangle:
                glVertex3f(*cube['vertices'][vertex])
        glEnd()



class CubeMatrix():

    # Um spaeter Sortfunktionen aufrufen zu koennen,
    # so muessen die Positiotionen gleich bei der
    # Initialisierung mitgespeichert werden!

    def __init__(self, size):

        # This Expression repressents a 3D-Matrix of Cube-Objects
        self.A = [[[Cube((i,j,k)) for k in  range(3)]for j in range(3)]for i in range(3)]
        # here we safe the played rounds
        self.rounds = []
        # We save the last gol object because of the check if fade in or out
        self.old_g = None

    def draw(self, g):
        if not self.old_g:
            self.old_g = g

        for i, area in enumerate(self.A):
            for j, row in enumerate(area):
                for k, cell in enumerate(row):
                    # Cell doen't is alive
                    if not g[i][j][k]:
                        continue
                    if g[i][j][k] == self.old_g[i][j][k]:
                        cell.draw()
                    else:
                        if self.old_g[i][j][k]:
                            cell.blend_out()
                        else:
                            cell.blend_in()

