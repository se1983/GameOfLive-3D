
cube_vertices = [(x, y, z) for x in (1, -1) for y in (1, -1) for z in (1, -1)]

def wired_cube():

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

    return dict(edges = edges, vertices = cube_vertices)

def triangled_cube():

    triangles = (
        (0,1,3),
        (0,1,5),
        (0,2,3),
        (0,2,6),
        (0,4,5),
        (0,4,6),
        (7,4,5),
        (7,4,6),
        (7,1,5),
        (7,1,3),
        (7,2,3),
        (7,2,6)
    )

    return dict(triangles = triangles, vertices = cube_vertices)