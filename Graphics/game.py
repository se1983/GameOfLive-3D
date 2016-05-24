import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from Graphics.geometrics import cube
from Graphics.objects import draw_cube_cube, draw_cube

class GameMain():
    # handles intialization of game and graphics, as well as game loop
    done = False

    def __init__(self, width=800, height=800):
        """Initialize PyGame window.

        variables:
            width, height = screen width, height
            screen = main video surface, to draw on

            fps_max = framerate limit to the max fps
            limit_fps = boolean toggles capping FPS, to share cpu, or let it run free.
            now = current time in Milliseconds. ( 1000ms = 1second)
        """
        pygame.init()

        # save w, h, and screen
        self.width, self.height = width, height
        self.screen = pygame.display.set_mode((self.width, self.height), DOUBLEBUF|OPENGL)
        pygame.display.set_caption( "GOL 3D" )

        gluPerspective(45, (self.width/self.height), 0.1, 50.0)
        glTranslatef(-10.0,-10.0, -10.0, -40)

        self.light_on = False
        glEnable( GL_LIGHTING )
        glEnable(GL_LIGHT1)
        glDisable(GL_LIGHT0)


        # Transparent objects



    def main_loop(self):
        """Game() main loop."""
        while not self.done:
            self.handle_events()
            self.update()
            self.draw()

    def draw(self):
        """draw screen"""

        # draw your stuff here. sprites, gui, etc....

        glRotatef(1, 3, 1, 1)

        # Transparent objects
        # Untested
        # http://stackoverflow.com/questions/23613715/drawing-transparent-subsurfaces-windows-in-pyopengl
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_BLEND)
        glPolygonOffset(1.0, 1.0)
        glEnable(GL_POLYGON_OFFSET_FILL)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        draw_cube_cube(cube(), 5)
        #draw_cube(cube())




        # Lightning
        if self.light_on:
            glLightfv( GL_LIGHT1, GL_AMBIENT, GLfloat_4(0.2, .2, .2, 1.0) )
            glLightfv(GL_LIGHT1, GL_DIFFUSE, GLfloat_3(.8,.8,.8))
            glLightfv(GL_LIGHT1, GL_POSITION, GLfloat_4(-2,0,3,1) )
        else:
            glDisable( GL_LIGHTING )
            glDisable(GL_LIGHT1)
            glDisable(GL_LIGHT0)

        pygame.display.flip()

    def update(self):
        """physics/move guys."""
        '''Here we are setting the lighting parameters'''


    def handle_events(self):
        """handle events: keyboard, mouse, etc."""
        events = pygame.event.get()
        kmods = pygame.key.get_mods()

        for event in events:
            if event.type == pygame.QUIT:
                self.done = True
            # event: keydown
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE: self.done = True