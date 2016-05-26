from Graphics.game import GameMain
from GOL.game import GameOfLife

from random import randint

if __name__ == "__main__":

    size = 5
    livings = [(randint(0, size-1), randint(0, size-1), randint(0, size-1)) for x in range(40)]

    gol = GameOfLife(size, livings, run=False)
    gol.start()

    game = GameMain(gol=gol, board_size=size)
    game.main_loop()
