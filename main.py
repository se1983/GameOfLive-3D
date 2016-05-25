from Graphics.game import GameMain
from GOL.game import GameOfLife

from random import randint

if __name__ == "__main__":

    size = 20
    livings = [(randint(0, size-1), randint(0, size-1), randint(0, size-1)) for x in range(500)]

    gol = GameOfLife(size, livings)

    game = GameMain(gol=gol, board_size=size)
    game.main_loop()
