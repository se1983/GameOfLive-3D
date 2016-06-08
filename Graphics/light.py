from OpenGL.GL import *
from OpenGL.GL import shaders
from OpenGL.GLU import *
from OpenGL.raw.GL.VERSION.GL_1_0 import glEnable, glFrustum
from pygame.locals import *

from Graphics import colors

def init():
    position = [100.5, 100.0, 100.0, 0.2]

    light_color = {'ambient' : GLfloat_4(*colors.grey),
                    'diffuse' : GLfloat_4(*colors.grey),
                    'specular': GLfloat_4(*colors.grey)
              }

    glLightfv(GL_LIGHT0, GL_POSITION, position)
    glLightfv(GL_LIGHT0, GL_AMBIENT, light_color['ambient'])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_color['diffuse'])
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_color['specular'])
    glLightfv(GL_LIGHT0, GL_QUADRATIC_ATTENUATION, (0.1,0,1))


    glLightfv(GL_LIGHT1, GL_POSITION, [-p for p in position])
    glLightfv( GL_LIGHT1, GL_AMBIENT, light_color['ambient'])
    glLightfv(GL_LIGHT1, GL_DIFFUSE, light_color['diffuse'])
    glLightfv(GL_LIGHT1, GL_SPECULAR, GLfloat_4(0,0.3,0, 1))
    glLightfv(GL_LIGHT1, GL_QUADRATIC_ATTENUATION, (0.1,1,0))
    # https://www.sjbaker.org/steve/omniv/opengl_lighting.html
    glEnable ( GL_COLOR_MATERIAL )

def draw(light_on):
        # Lightning
    if light_on:
        glEnable( GL_LIGHTING )
        glEnable(GL_LIGHT1)
        glEnable(GL_LIGHT0)
    else:
        glDisable( GL_LIGHTING )
        glDisable(GL_LIGHT1)
        glDisable(GL_LIGHT0)


