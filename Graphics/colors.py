dark_green = (0.0, 0.6, 0.0)
blue = (0,0,1)
green = (0.0, 1, 0.0)
red = (1, 0, 0)
grey = (0.3, 0.3, 0.3)
dark_grey = (0.2, 0.2, 0.2)
white = (1, 1, 1)
black = (0, 0, 0)
cyan = (0, 1, 1)
magenta = (1, 0, 1)
yellow = (1, 1, 0)

heatmap = [black, blue, cyan, green, yellow, red, white]

draw = {
    'background': black + (1,),
    'wires': white,
    'surface': white,
    'die': red,
    'born': green,
    'light_0' :{
        'ambi' : white,
        'diff' : white,
        'spec' : white
    },
    'light_1' :{
        'ambi' : white,
        'diff' : white,
        'spec' : white
    }
}
