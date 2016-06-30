
from OpenGL.GL import *
from OpenGL.raw.GL.ARB.tessellation_shader import GL_TRIANGLES

from Graphics import colors, geometrics


class Cube():

    def __init__(self, position):
        self.cube = geometrics.cube()
        self.alpha = 0.5
        self.position = position
        self.status = 'draw'
        self.alpha_range = [a_value/1000 for a_value in range(1000)]

    def draw(self):

        glTranslatef(*self.__translation(+2.1))
        self.__draw_wired_cube(colors.grey, self.alpha)
        self.__draw_triangled_cube(colors.green, self.alpha)
        glTranslatef(*self.__translation(-2.1))


    def __translation(self, factor):
        return [(factor * n) for n in self.position]



    def blend_in(self):
        self.status = 'blend_in'
        self.draw()

    def blend_out(self):
        self.status = 'blend_out'
        self.draw()

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
        self.A = [[[Cube((i,j,k))
                    for k in range(size)]
                   for j in range(size)]
                  for i in range(size)]
        # here we safe the played rounds
        self.rounds = []
        # We save the last gol object because of the check if fade in or out
        self.old_g = None
        self.size = size

    def draw(self, g):
        if not self.old_g:
            self.old_g = g


        print(self.size)
        glTranslatef(*[self.size * -2.1 * 0.5 for _ in range(3)])

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
        glTranslatef(*[self.size * 2.1 * 0.5 for _ in range(3)])


