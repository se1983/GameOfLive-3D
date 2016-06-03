import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GL import shaders
from OpenGL.GLU import *
from OpenGL.raw.GL.VERSION.GL_1_0 import glEnable, glFrustum

from Graphics.geometrics import cube
from Graphics.objects import draw_cube_Matrix
from Graphics.shader import vertex,fragment
from Graphics import colors, light

from time import sleep

class GameMain():
    # handles intialization of game and graphics, as well as game loop
    done = False

    def __init__(self, gol, width=800, height=800, board_size=5):
        """Initialize PyGame window.

        variables:
            width, height = screen width, height
            screen = main video surface, to draw on

            fps_max = framerate limit to the max fps
            limit_fps = boolean toggles capping FPS, to share cpu, or let it run free.
            now = current time in Milliseconds. ( 1000ms = 1second)
        """
        self.demo_mode = True
        self.interact_mode = False
        self.demo_speed = 1
        self.light_on = False
        self.board_size = board_size

        self.gol = gol

        pygame.init()

        # save w, h, and screen
        self.width, self.height = width, height
        self.screen = pygame.display.set_mode((self.width, self.height), OPENGL)
        pygame.display.set_caption( "sebsch's 3D LIFE <%s>" % "".join([str(i) for i in self.gol.ruleset]))

        gluPerspective(45, (self.width/self.height), 0.1, 12.0 * self.board_size)
        # positioning
        self.__init_position()
        # Light
        self.__init_light__()
        # Z-Filter
        self.__init_zfilter__()
        # Transparent objects
        self.__init_alpha__()
        # Offset for better displaying
        self.__init_polyoffset()



    def __init_position(self):
        glTranslatef(-2.5,-2.5, -8.0 * self.board_size, 1 )
        glRotatef(45, 1,0,1)


    def __init_light__(self):

        # TODO: light looks terrible! looking just for shiny reflections
        # Even with GL_SMOOTH there are Phong-reflections
        light.init()

    def __init_zfilter__(self):
        glEnable( GL_DEPTH_TEST )
        glEnable(GL_STENCIL_TEST)

    def __init_alpha__(self):
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_BLEND)

    def __init_polyoffset(self):
        glPolygonOffset(1.0, 1.0)
        glEnable(GL_POLYGON_OFFSET_FILL)

    def main_loop(self):
        """Game() main loop."""
        while not self.done:
            self.handle_events()
            self.update()
            self.draw()
            sleep(0.01)

    def draw(self):
        """draw screen"""

        # draw your stuff here. sprites, gui, etc....

        if self.demo_mode:
            glRotatef(self.demo_speed, 3, 1, 1)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT | GL_STENCIL_BUFFER_BIT)
        glClearColor(0.1,0.2,0.1,1)
        draw_cube_Matrix(cube(), self.board_size, g=self.gol.g)

        # Lightning
        if self.light_on:
            glEnable( GL_LIGHTING )
            glEnable(GL_LIGHT1)
            glEnable(GL_LIGHT0)
        else:
            glDisable( GL_LIGHTING )
            glDisable(GL_LIGHT1)
            glDisable(GL_LIGHT0)

        pygame.display.flip()

    def update(self):
        """physics/move guys."""
        if self.interact_mode:
            x, y = pygame.mouse.get_rel()
            glRotatef(x, 0,1,0)
            glRotatef(y, 0,0,1)



    def toggle_light(self):
        self.light_on = not self.light_on

    def handle_events(self):
        """handle events: keyboard, mouse, etc."""
        events = pygame.event.get()
        kmods = pygame.key.get_mods()
        mousebutton_pressed = False

        for event in events:

            if event.type == pygame.QUIT:
                self.done = True
            # event: keydown

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.done = True
                    self.gol.kill()
                if event.key == K_SPACE:
                    self.gol.tick()
                if event.key == K_l:
                    self.toggle_light()


            ## Mousebutton 1 (left) klicked starts the interactive mode
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.demo_mode = False
                self.interact_mode = True
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.demo_mode = True
                self.interact_mode = False
            ## Mousebutton left release ends the interactive mode
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
                glTranslatef(0,1,1, 1 )
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
                glTranslatef(0,-1,-1, 1 )

