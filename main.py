from GOL.game import GameOfLife
from Graphics.geometrics import cube

gol = GameOfLife([2,2,2], ((1,1,1),(1,0,0),(1,2,2)))

for point in gol.g:
    print(point)

for vertex in cube():
    print(vertex)
