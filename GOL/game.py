from threading import Thread

from time import sleep


class GameOfLife(Thread):
    def __init__(self, n, livings, run=False, ruleset='2555'):

        Thread.__init__(self)
        self.__run = run
        self.ruleset = [int(s) for s in ruleset]

        # This helps to generalise.
        # As standard n should be a 3d-list but if it's just integer we make one.
        if type(n) == int:
            n = [n, n, n]
        self.size = n[0]

        # get True if alive and False if dead
        self.g = [[[(x, y, z) in livings for x in xrange(n[0])] for y in xrange(n[1])] for z in xrange(n[2])]
        self.n = n

    def run(self):
        self.__main_loop()

    def kill(self):
        self.__run = False

    def tick(self):
        """ Next step
        :return:
        """
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
                        # check the sides
                        if self.g[i][j][k + 1]:
                            n[i][j][k] += 1
                        if self.g[i][j][k - 1]:
                            n[i][j][k] += 1
                        if self.g[i][j + 1][k]:
                            n[i][j][k] += 1
                        if self.g[i][j - 1][k]:
                            n[i][j][k] += 1
                        if self.g[i + 1][j][k]:
                            n[i][j][k] += 1
                        if self.g[i - 1][j][k]:
                            n[i][j][k] += 1
                        # counting also the neighbors
                        # on the edges
                        if self.g[i + 1][j + 1][k + 1]:
                            n[i][j][k] += 1
                        if self.g[i - 1][j + 1][k + 1]:
                            n[i][j][k] += 1
                        if self.g[i + 1][j - 1][k + 1]:
                            n[i][j][k] += 1
                        if self.g[i - 1][j - 1][k + 1]:
                            n[i][j][k] += 1
                        if self.g[i + 1][j + 1][k - 1]:
                            n[i][j][k] += 1
                        if self.g[i - 1][j + 1][k - 1]:
                            n[i][j][k] += 1
                        if self.g[i + 1][j - 1][k - 1]:
                            n[i][j][k] += 1
                        if self.g[i - 1][j - 1][k - 1]:
                            n[i][j][k] += 1
                        if self.g[i + 1][j + 1][k]:
                            n[i][j][k] += 1
                        if self.g[i - 1][j + 1][k]:
                            n[i][j][k] += 1
                        if self.g[i + 1][j - 1][k]:
                            n[i][j][k] += 1
                        if self.g[i - 1][j - 1][k]:
                            n[i][j][k] += 1
                    except IndexError:
                        # ignore the edges
                        pass
        return n

    def __game(self, g):
        """
        Here lives the cellular automate.

        Checking the ruleset by the wxyz-notation.

        :return: g -- game object
        """

        n = self.neighbor_count()

        # Life wxyz is the rule set in which an alive cell will
        # stay alive in the next generation if it has n live neighbors
        # and w <= n <= x and a dead cell will become alive in the
        # next generation if y <= n <= z.

        ## @TODO automate in expression

        for i, area in enumerate(self.g):
            for j, row in enumerate(area):
                for k, cell in enumerate(row):
                    if cell:
                        if not (self.ruleset[0] <= n[i][j][k] <= self.ruleset[1]):
                            self.g[i][j][k] = False
                    else:
                        if self.ruleset[2] <= n[i][j][k] <= self.ruleset[3]:
                            self.g[i][j][k] = True
        return g

    def __main_loop(self):
        while self.__run:
            sleep(1)
            self.tick()
