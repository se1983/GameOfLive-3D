from threading import Thread

from time import sleep


class GameOfLife(Thread):
    def __init__(self, n, livings, runner=False, ruleset='2555'):

        Thread.__init__(self)
        self.runner = runner
        self.done = False
        self.ruleset = [int(s) for s in ruleset]

        # get True if alive and False if dead
        self.g = [[[(x, y, z) in livings for x in xrange(n)] for y in xrange(n)] for z in xrange(n)]
        self.n = n
        self.size = n
        self.neighbors = self.neighbor_count()


    def run(self):
        self.__main_loop()

    def kill(self):
        self.done = True

    def __main_loop(self):
        while not self.done:
            sleep(1)
            if self.runner:
                self.tick()
    def toggle_run(self):
        self.runner = not self.runner


    def tick(self):
        """ Next step
        :return:
        """
        self.g = self.__game(self.g)

    def neighbor_count(self):
        """

        :return: Matrix of the neighbors
        """

        n = [[[0 for x in xrange(self.n)] for y in xrange(self.n)] for z in xrange(self.n)]

        for i, a in enumerate(self.g):
            for j, r in enumerate(a):
                for k, e in enumerate(r):
                    # check the sides
                    if (not k >= self.size-1):
                        if self.g[i][j][k + 1]:
                            n[i][j][k] += 1
                    if (not k <= 0):
                        if self.g[i][j][k - 1]:
                            n[i][j][k] += 1
                    if (not j >= self.size-1):
                        if self.g[i][j + 1][k]:
                            n[i][j][k] += 1
                    if (not j <= 0):
                        if self.g[i][j - 1][k]:
                            n[i][j][k] += 1
                    if (not i >= self.size-1):
                        if self.g[i + 1][j][k]:
                            n[i][j][k] += 1
                    if (not i <= 0):
                        if self.g[i - 1][j][k]:
                            n[i][j][k] += 1
                    # counting also the neighbors
                    # on the edges
                    if (not i >= self.size-1) and (not j >= self.size-1) and (not k >= self.size-1):
                        if self.g[i + 1][j + 1][k + 1]:
                            n[i][j][k] += 1
                    if (not i <= 0) and (not j >= self.size-1) and (not k >= self.size-1):
                        if self.g[i - 1][j + 1][k + 1]:
                            n[i][j][k] += 1
                    if (not i >= self.size-1) and (not j <= 0) and (not k >= self.size-1):
                        if self.g[i + 1][j - 1][k + 1]:
                            n[i][j][k] += 1
                    if (not i <= 0) and (not j <= 0) and (not k >= self.size-1):
                        if self.g[i - 1][j - 1][k + 1]:
                            n[i][j][k] += 1
                    if (not i >= self.size-1) and (not j >= self.size-1) and (not k <= 0):
                        if self.g[i + 1][j + 1][k - 1]:
                            n[i][j][k] += 1
                    if (not i <= 0) and (not j >= self.size-1) and (not k <= 0):
                        if self.g[i - 1][j + 1][k - 1]:
                            n[i][j][k] += 1
                    if (not i >= self.size-1) and (not j >= 0) and (not k <= 0):
                        if self.g[i + 1][j - 1][k - 1]:
                            n[i][j][k] += 1
                    if (not i <= 0) and (not j <= 0) and (not k <= 0):
                        if self.g[i - 1][j - 1][k - 1]:
                            n[i][j][k] += 1
                    if (not i >= self.size-1) and  (not j >= self.size-1):
                        if self.g[i + 1][j + 1][k]:
                            n[i][j][k] += 1
                    if (not i <= 0) and (not j >= self.size-1):
                        if self.g[i - 1][j + 1][k]:
                            n[i][j][k] += 1
                    if (not i >= self.size-1) and (not j <= 0):
                        if self.g[i + 1][j - 1][k]:
                            n[i][j][k] += 1
                    if (not i <= 0) and (not j <= 0):
                        if self.g[i - 1][j - 1][k]:
                            n[i][j][k] += 1
        return n

    def __game(self, g):
        """
        Here lives the cellular automate.

        Checking the ruleset by the wxyz-notation.

        :return: g -- game object
        """

        self.neighbors = self.neighbor_count()

        # Life wxyz is the rule set in which an alive cell will
        # stay alive in the next generation if it has n live neighbors
        # and w <= n <= x and a dead cell will become alive in the
        # next generation if y <= n <= z.

        # n is here self.neighbors
        # w,x,y,z are handled via ruleset[0-3]

        for i, area in enumerate(self.g):
            for j, row in enumerate(area):
                for k, cell in enumerate(row):
                    if cell:
                        if not (self.ruleset[0] <= self.neighbors[i][j][k] <= self.ruleset[1]):
                            self.g[i][j][k] = False
                    else:
                        if self.ruleset[2] <= self.neighbors[i][j][k] <= self.ruleset[3]:
                            self.g[i][j][k] = True
        return g

