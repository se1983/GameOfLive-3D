white = (1, 1, 1)
black = (0, 0, 0)

red = (1, 0, 0)
green = (0.0, 1, 0.0)
blue = (0, 0, 1)

cyan = (0, 1, 1)
magenta = (1, 0, 1)
yellow = (1, 1, 0)

grey = (0.3, 0.3, 0.3)
dark_grey = (0.2, 0.2, 0.2)
dark_green = (0.0, 0.6, 0.0)



def ipol(col_1, col_2):
    return tuple([(col_1[c] + col_2[c]) * 1 / 2.0 for c in range(len('rgb'))])


heatmap = [
    blue,
    ipol(blue, cyan),
    cyan,
    ipol(cyan, green),
    green,
    ipol(green, yellow),
    yellow,
    ipol(yellow, red),
    red,
    ipol(red, magenta),
    magenta,
    ipol(magenta, white),
    white]

draw = {
    'background': black + (1,),
    'wires': white,
    'surface': white,
    'die': dark_grey,
    'born': grey,
    'light_0': {
        'ambi': white,
        'diff': white,
        'spec': white
    },
    'light_1': {
        'ambi': white,
        'diff': white,
        'spec': white
    }
}
