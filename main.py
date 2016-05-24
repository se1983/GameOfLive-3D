from Graphics.game import GameMain
from GOL.game import GameOfLife

if __name__ == "__main__":

    size = 5
    livings = [(0,0,0), (0,0,1), (0,1,1), (3,4,2), (2,4,1)]

    gol = GameOfLife(size, livings)

    game = GameMain(gol=gol, board_size=size)
    game.main_loop()
