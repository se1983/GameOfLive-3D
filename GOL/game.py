from threading import Thread

from time import sleep


class GameOfLife(Thread):

    def __init__(self, n, beings, run=False):

        Thread.__init__(self)
        self.run = run

        # This helps to generalise.
        # As standard n should be a 3d-list but if it's just integer we make one.
        if type(n) == int:
            n = [n,n,n]
        # Check the dimensions
        if not len(n) == 3:
            raise AttributeError('This is a 3D GOL. Give a list with 3 or just 1 value!')
        # Generate a 3 dimensional list of False-Values

        # get True if alive and False if dead
        self.g = [[[(x, y, z) in beings for x in xrange(n[0])] for y in xrange(n[1])] for z in xrange(n[2])]

    def run(self):
        self.__main_loop()



    def tick(self):
        """ Next step
        :return:
        """
        # @TODO Make me a iterator object

        self.g = self.__game(self.g)

    def neighbor_count(self):
        """

        :return: Matrix of the neighbors
        """
        n = 0

    def __game(self, g):
        """
        applied regulations
        :return: None
        """

        # Using the ruleset (2555)
        # http://www.complex-systems.com/pdf/05-1-2.pdf
        # http://www.complex-systems.com/pdf/08-1-4.pdf

        # Safe Environment
        # With range (2,5) neighbors a living cell keeps alive
        # 2 5
        # fertility
        # Wit 5 neighbors a dead cell gets alive
        # 5 5

        # 1. count neighbors
        # 2. is alive & not neighbors in range(2,5)  -> die!
        # 3. is dead & neighbors == 5 -> life!

        return g

    def __main_loop(self):
        while self.run:
            sleep(3)
            self.tick()







