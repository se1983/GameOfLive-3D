
def cube():

    vertices = [(x,y,z) for x in (1,-1) for y in (1,-1) for z in (1,-1)]

    edges = (
        (0, 1),
        (0, 2),
        (0, 4),
        (3, 2),
        (3, 1),
        (3, 7),
        (5, 1),
        (5, 4),
        (5, 7),
        (6, 2),
        (6, 7),
        (6, 4)
    )

    return dict(edges = edges, vertices = vertices)