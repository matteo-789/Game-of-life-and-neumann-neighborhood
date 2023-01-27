import pygame
from numpy.random import default_rng
import numpy as np
import argparse
from neumann_neighborhood import set_neumann_neighb, apply_rule_neumann
from game_of_life import set_upgol, apply_rule_gol

# Simulation And Application Settings
long = 500
larg = 600
cellSize = 4
long_arr = int(long/cellSize)
larg_arr = int(larg/cellSize)
generationTimestep = 10

def main(args):
    pygame.init()
    screen = pygame.display.set_mode((larg, long))
    pygame.display.set_caption("Cellular Automata")
    done = False
    clock = pygame.time.Clock()
    cells = np.zeros((long_arr, larg_arr), dtype=int)
    generation = 0
    screen.fill((255, 255, 255))

    if args.x != None:
        set_upgol(screen, cells, cellSize, larg_arr, long_arr, args.x)
    else:
        set_neumann_neighb(screen, cells, cellSize, larg_arr, long_arr)
    while not done:
        if args.x != None:
            cells = apply_rule_gol(screen, cells, cellSize, larg_arr, long_arr)
        else:
            cells = apply_rule_neumann(screen, cells, cellSize, larg_arr, long_arr)

        pygame.display.update()
        generation += 1
        clock.tick(generationTimestep)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True


if __name__ == "__main__":
    # create the top-level parser
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    # create the parser for the "gol" command
    parser_gol = subparsers.add_parser('gol')
    parser_gol.add_argument('-x', type=int, default=50, help="Set number for generation")

    # create the parser for the "neumann" command
    parser_neumann = subparsers.add_parser('neumann')
    parser_neumann.add_argument('-x', default=None, help="Please let this to default")

    args = parser.parse_args()
    main(args)
    pygame.quit()
