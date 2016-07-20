import sys

from Graphics.game import GameMain
from GOL.game import GameOfLife

from random import randint



# DONE Wuerfel zeichnen
# DONE Life-Automat
# Done Zell-Matrix zeichnen
# Done Beleuchtung
# Done Zoom und drehen durch Maus
# Done Uebergaenge l->d / d->l
# Done autorun


def main():
    size = 16
    beeings = 600
    # no twins allowed, the second dies
    livings = [(randint(0, size-1),
                randint(0, size-1),
                randint(0, size-1)) for x in range(beeings)]

    gol = GameOfLife(size, livings, runner=False, ruleset="2555")
    #gol = GameOfLife(size, livings, runner=True, ruleset="5655")
    gol.start()
    game = GameMain(gol=gol)
    game.main_loop()
    gol.kill()



if __name__ == "__main__":
    main()