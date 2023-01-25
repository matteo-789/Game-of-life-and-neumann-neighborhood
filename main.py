import pygame
from numpy.random import default_rng
import numpy as np
from neumann_neighborhood import set_neumann_neighb, apply_rule_neumann
from glider import set_upgol, apply_rule_gol

# Simulation And Application Settings
long = 500
larg = 600
cellSize = 4
long_arr = int(long/cellSize)
larg_arr = int(larg/cellSize)
generationTimestep = 10

def main():
    pygame.init()
    screen = pygame.display.set_mode((larg, long))
    pygame.display.set_caption("Cellular Automata")
    done = False
    clock = pygame.time.Clock()
    cells = np.zeros((long_arr, larg_arr), dtype=int)
    generation = 0
    screen.fill((255, 255, 255))

    #set_neumann_neighb(screen, cells, cellSize, larg_arr, long_arr)
    set_upgol(screen, cells, cellSize, larg_arr, long_arr)
    while not done:
        cells = apply_rule_gol(screen, cells, cellSize, larg_arr, long_arr)
        #cells = apply_rule_neumann(screen, cells, cellSize, larg_arr, long_arr)

        pygame.display.update()
        generation += 1
        clock.tick(generationTimestep)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True


if __name__ == "__main__":
    main()
    pygame.quit()
