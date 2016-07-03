from Graphics.game import GameMain
from GOL.game import GameOfLife

from random import randint


""" FRAGEN
3. Elemente aus der Beleuchtung ausnehmen (HUD)
"""

# DONE Wuerfel zeichnen
# DONE Life-Automat
# Done Zell-Matrix zeichnen
# Done Beleuchtung
# Done Zoom und drehen durch Maus
# Done Uebergaenge l->d / d->l
# TODO HUD
# TODO Steuerung durch config-files
# TODO autorun

if __name__ == "__main__":

    size = 16
    beeings = 400
    # no twins allowed, the second dies
    livings = [(randint(0, size-1),
                randint(0, size-1),
                randint(0, size-1)) for x in range(beeings)]

    gol = GameOfLife(size, livings, run=True, ruleset="2555")
    #gol = GameOfLife(size, livings, run=True, ruleset="5655")

    gol.start()

    game = GameMain(gol=gol)
    game.main_loop()
