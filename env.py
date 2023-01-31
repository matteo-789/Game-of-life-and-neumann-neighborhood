from numpy.random import default_rng

#set random generator
rng = default_rng()
rdn = default_rng()

#set colors for screen
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
RGB = (RED, GREEN, BLUE)

#set global screen options
height = 800
width = 900
cellSize = 4
height_arr = int(height/cellSize)
width_arr = int(width/cellSize)
generationTimestep = 10
