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
        self.n = n

        # Check the dimensions
        if not len(n) == 3:
            raise AttributeError('This is a 3D GOL. Give a list with 3 or just 1 value!')
        # Generate a 3 dimensional list of False-Values

        # get True if alive and False if dead
        self.g = [[[(x, y, z) in beings for x in xrange(n[0])] for y in xrange(n[1])] for z in xrange(n[2])]
        print(self.g)

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

        n = [[[0 for x in xrange(self.n[0])] for y in xrange(self.n[1])] for z in xrange(self.n[2])]

        for i, a in enumerate(self.g):
            for j, r in enumerate(a):
                for k, e in enumerate(r):
                    try:
                        if self.g[i][j][k+1]:
                            n[i][j][k] += 1
                        if self.g[i][j][k-1]:
                            n[i][j][k] += 1
                        if  self.g[i][j+1][k]:
                            n[i][j][k] += 1
                        if self.g[i][j-1][k]:
                            n[i][j][k] += 1
                        if self.g[i+1][j][k]:
                            n[i][j][k] += 1
                        if self.g[i-1][j][k]:
                            n[i][j][k] += 1
                    except IndexError:
                        pass
        print(n)
        return n





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
        n = self.neighbor_count()
        # 2. is alive & not neighbors in range(2,5)  -> die!

        ## Here we use RULESET: 4555

        # Life wxyz is the rule set in which an alive cell will
        # stay alive in the next generation if it has n live neighbors
        # and w ≤ n ≤ x and a dead cell will become alive in the next generation if y ≤ n ≤ z.

        for i, a in enumerate(self.g):
            for j, r in enumerate(a):
                for k, e in enumerate(r):
                    if self.g[i][j][k]:
                        if  (n[i][j][k] < 4 or n[i][j][k] > 5):
                            self.g[i][j][k] = False
                    else:
                        if n[i][j][k] == 5:
                            self.g[i][j][k] = True
        print(g)
        return g

    def __main_loop(self):
        while self.run:
            sleep(3)
            self.tick()







