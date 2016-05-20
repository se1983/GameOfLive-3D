

class GameOfLife(object):

    def __init__(self, n, beings):

        # This helps to generalise.
        # As standard n should be a 3d-list but if it's just integer we make one.
        if type(n) == int:
            n = [n,n,n]
        # Check the dimensions
        if not len(n) == 3:
            raise AttributeError('This is a 3D GOL. Give a list with 3 or just 1 value!')
        # Generate a 3 dimensional list of False-Values

        self.playing_space = [[[(k,j,i) in beings for k in xrange(n[0])] for j in xrange(n[1])] for i in xrange(n[2])]


    def tick(self):
        """ Next step
        :return:
        """
        # @TODO Make me a iterator object
        pass

    def neighbor_count(self):
        """

        :return: Matrix of the neighbors
        """
        pass

    def __game(self, space):
        """
        applied regulations
        :return: A new Game
        """

        # Using the following ruleset (2555)
        # http://www.complex-systems.com/pdf/05-1-2.pdf
        # http://www.complex-systems.com/pdf/08-1-4.pdf

        # Safe Environment
        # With range (2,5) neighbors a living cell keeps alive
        # 2 5
        # fertility
        # Wit 5 neighbors a dead cell gets alive
        # 5 5






