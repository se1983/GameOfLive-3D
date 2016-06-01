from Graphics.game import GameMain
from GOL.game import GameOfLife

from random import randint

if __name__ == "__main__":

    size = 7
    livings = [(randint(0, size-1), randint(0, size-1), randint(0, size-1)) for x in range(100)]

    gol = GameOfLife(size, livings, run=False, ruleset="2555")
    gol.start()

    game = GameMain(gol=gol, board_size=size)
    game.main_loop()
