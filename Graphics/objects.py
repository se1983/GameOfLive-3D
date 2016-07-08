from OpenGL.GL import *
from OpenGL.raw.GL.ARB.tessellation_shader import GL_TRIANGLES

from Graphics import colors, geometrics

from math import sin, pi, e
from copy import deepcopy


# List of values for the alpha_blending
f = lambda x: sin(x)
frames = 10.0
A = [f(n / frames) for n in range(int(pi / 2 * frames))]

class Cube():

    def __init__(self, position):
        self.cube = geometrics.cube()
        self.position = position
        self.status = 'draw'
        self.surface_color = colors.draw['surface']
        self.wire_color = colors.draw['wires']
        self.alpha_range = A
        self.alpha = self.alpha_range[-1]

    def draw(self, neighbors=-1):

        glTranslatef(*self.__translation(+2.1))
        #self.__draw_wired_cube(self.wire_color)
        if self.status == 'draw' and not neighbors < 0:
            self.surface_color = colors.heatmap[neighbors][0:4]
        if neighbors == -1:
            self.surface_color = colors.draw['surface']

        self.__draw_triangled_cube(self.surface_color)
        self.__fader()
        glTranslatef(*self.__translation(-2.1))

    def __fader(self):
        """
        Iterating over values for alphablending.

        Values are defined global in this module.
        :return: :None
        """
        if self.status == 'draw':
            return
        i = self.alpha_range.index(self.alpha)
        if self.status == 'blend_in':
            i += 1
        elif self.status == 'blend_out':
            i -= 1
            # -1 don't throws IndexError so
            # we have to handle this here.
            if i <= -1:
                self.status = 'draw'
                i = len(A)
                return
        try:
            self.alpha = self.alpha_range[i]
        except IndexError:
            self.status = 'draw'
            self.surface_color = colors.draw['surface']


    def __translation(self, factor):
        return [(factor * n) for n in self.position]

    def blend_in(self):
        self.surface_color = colors.draw['born']
        self.alpha = self.alpha_range[0]
        self.status = 'blend_in'

    def blend_out(self):
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
        glColor4f(*color[0:4])

        for i, triangle in enumerate(cube['triangles']):
            glNormal3f(*cube['normals'][i])
            for vertex in triangle:
                glVertex3f(*cube['vertices'][vertex])
        glEnd()


class CubeMatrix():

    def __init__(self, gol):

        # This Expression repressents a 3D-Matrix of Cube-Objects
        self.playground = [[[Cube((i, j, k))
                             for k in range(gol.size)]
                            for j in range(gol.size)]
                           for i in range(gol.size)]
        # Saving the g-Matrix
        self._g = deepcopy(gol.g)
        # The size of the playground
        self.size = gol.size * -2.1

    def draw(self, gol, FX_appear=True, FX_disappear=True, heatmap=True):

        # saving the state of gol's g
        g = deepcopy(gol.g)
        # translation for centric universe
        glTranslatef(*[self.size * 0.5 + 1 for _ in range(len('xyz'))])

        for i, area in enumerate(self.playground):
            for j, row in enumerate(area):
                for k, cell in enumerate(row):
                    new = g[i][j][k]
                    old = self._g[i][j][k]

                    # Status 'blend_out' also means the object
                    # is most likely not existing in g and _g
                    # so we ignore it here.
                    if not new and not old and not cell.status == 'blend_out':
                        continue

                    # dying and bearing
                    if (not new) and old and FX_disappear:
                        cell.blend_out()
                    if new and (not old) and FX_appear:
                        cell.blend_in()
                    # Show the cell.
                    if heatmap:
                        cell.draw(gol.neighbors[i][j][k])
                    else:
                        cell.draw(-1)
        self._g = deepcopy(g)
        # Translation back in the Center
        glTranslatef(*[self.size * -0.5 - 1 for _ in range(len('xyz'))])
