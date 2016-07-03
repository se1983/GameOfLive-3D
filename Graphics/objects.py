from OpenGL.GL import *
from OpenGL.raw.GL.ARB.tessellation_shader import GL_TRIANGLES

from Graphics import colors, geometrics

from math import sin, pi, e
from copy import deepcopy

f = lambda x: sin(x)
grans = 10.0
A = [f(n/grans) for n in range(int(pi/2 * grans))]

class Cube():

    def __init__(self, position):
        self.cube = geometrics.cube()
        self.position = position
        self.status = 'draw'
        self.suface_color = colors.draw['surface']
        self.wire_color = colors.draw['wires']
        self.alpha_range = A
        self.alpha = self.alpha_range[-1]

    def draw(self):

        glTranslatef(*self.__translation(+2.1))
        #self.__draw_wired_cube(self.wire_color)
        self.__draw_triangled_cube(self.suface_color)
        self.__fader()
        glTranslatef(*self.__translation(-2.1))

    def __fader(self):

        if self.status == 'draw':
            return

        i = self.alpha_range.index(self.alpha)

        if self.status == 'blend_in':
            i += 1
        elif self.status == 'blend_out':
            i -= 1

        try:
            self.alpha = self.alpha_range[i]
        except IndexError:
            self.status = 'draw'
            self.surface_color = colors.draw['surface']

    def __translation(self, factor):
        return [(factor * n) for n in self.position]

    def blend_in(self):
        self.alpha = self.alpha_range[0]
        self.status = 'blend_in'

    def blend_out(self):
        #self.alpha = self.alpha_range[-1]
        self.surface_color = colors.draw['die']
        self.status = 'blend_out'

    def __draw_wired_cube(self, color):
        cube = geometrics.wired_cube()

        glBegin(GL_LINES)
        color += (self.alpha,)
        glColor4f(*color)
        for edge in cube['edges']:
            for vertex in edge:
                glVertex3f(*cube['vertices'][vertex])
        glEnd()

    def __draw_triangled_cube(self, color):
        cube = geometrics.triangled_cube()
        glBegin(GL_TRIANGLES)
        color += (self.alpha,)
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

    def __init__(self, gol):

        # This Expression repressents a 3D-Matrix of Cube-Objects
        self.playground = [[[Cube((i, j, k))
                             for k in range(gol.size)]
                            for j in range(gol.size)]
                           for i in range(gol.size)]
        # here we safe the played rounds
        # We save the last gol object because of the check if fade in or out

        # mem of the last round
        self._g = deepcopy(gol.g)
        self.size = gol.size * -2.1

    def draw(self, gol):
        g = deepcopy(gol.g)

        glTranslatef(*[self.size * 0.5 + 1 for _ in range(len('xyz'))])

        for i, area in enumerate(self.playground):
            for j, row in enumerate(area):
                for k, cell in enumerate(row):

                    new = g[i][j][k]
                    old = self._g[i][j][k]

                    #if cell.status == 'blend_out':
                    #    cell.draw()
                    #    continue

                    if not new and not old:
                        continue

                    if (not new) and old:
                        cell.blend_out()

                    if new and (not old):
                        cell.blend_in()

                    cell.draw()
        self._g = g

        glTranslatef(*[self.size * -0.5 - 1 for _ in range(len('xyz'))])
