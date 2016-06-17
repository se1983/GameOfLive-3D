import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GL import shaders
from OpenGL.GLU import *
from OpenGL.raw.GL.VERSION.GL_1_0 import glEnable, glFrustum

from Graphics.geometrics import cube, wired_cube
from Graphics.objects import draw_cube_Matrix, draw_coord
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
        self.light_on = True
        self.alpha = 1
        self.board_size = board_size
        self.eye_distance = 10

        self.gol = gol

        pygame.init()

        # save w, h, and screen
        self.width, self.height = width, height
        self.screen = pygame.display.set_mode((self.width, self.height), OPENGL)
        pygame.display.set_caption( "sebsch's 3D LIFE <%s>" % "".join([str(i) for i in self.gol.ruleset]))
        gluPerspective(45, (self.width/self.height), 0.1, 10.0 * self.board_size)

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
        glMatrixMode(GL_PROJECTION);
        glFrustum(-1.0, 1.0, -1.0, 1.0, 1.5, 200.0);
        glMatrixMode(GL_MODELVIEW)

    def __init_light__(self):
        light.init()

    def __init_zfilter__(self):
        glEnable( GL_DEPTH_TEST )
        glEnable(GL_STENCIL_TEST)


    def __init_alpha__(self):
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_BLEND)
        glAlphaFunc ( GL_GREATER, 0.1 )
        glEnable(GL_ALPHA_TEST)


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

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
        color  = colors.grey + (0.3,)
        glClearColor(*color)
        draw_cube_Matrix(cube(), self.board_size, g=self.gol.g, alpha=self.alpha)

        light.draw(self.light_on)
        pygame.display.flip()



    def update(self):
        """physics/move guys."""
            ## zoom mit glLookat()
        glLoadIdentity()
        gluLookAt(  0, 0, self.eye_distance,   # x,y,z Position Eye
                    0, 0, 0,     # x,y,z Centering
                    0, 1, 0)     # x,y,z Vec - UP

        self.demo_speed += 1
        if self.demo_mode:
            glRotatef(self.demo_speed, 3, 1, 1)


        if self.interact_mode:
            x, y = pygame.mouse.get_pos()
            glRotatef(x, 0,1,0)
            glRotatef(y, 0,0,1)




    def toggle_light(self):
        self.light_on = not self.light_on

    def set_alpha(self, val):
        if self.alpha + val < 0:
            self.alpha = 0
        elif self.alpha + val > 1:
            self.alpha = 1
        else:
            self.alpha += val

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
                if event.key == K_f:
                    pygame.display.toggle_fullscreen()
                if event.key == K_a:
                    self.set_alpha(val = -0.1)
                if event.key == K_q:
                    self.set_alpha(val = +0.1)



            ## Mousebutton 1 (left) klicked starts the interactive mode
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.demo_mode = False
                self.interact_mode = True
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.demo_mode = True
                self.interact_mode = False
            ## Mousebutton left release ends the interactive mode
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
                #glTranslatef(0,1,1, 1 )
                self.eye_distance -= 0.3

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
                #glTranslatef(0,-1,-1, 1 )
                self.eye_distance += 0.3

