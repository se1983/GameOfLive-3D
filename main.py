from GOL.Game import GameOfLife

gol = GameOfLife([2,2,2], ((1,1,1),(1,0,0),(1,2,2)))

for point in gol.distance:
    print(point)