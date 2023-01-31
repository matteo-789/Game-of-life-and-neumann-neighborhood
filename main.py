import pygame
import numpy as np
import argparse
from neumann_neighborhood import set_neumann_neighb, apply_rule_neumann
from game_of_life import set_upgol, apply_rule_gol
from chaos import set_upchaos, apply_rule_chaos
from env import *

def set_functions(args):
    if args.commands == "gol":
        return set_upgol, apply_rule_gol, args.x, None
    elif args.commands == "neumann":
        return set_neumann_neighb, apply_rule_neumann, None, None
    elif args.commands == "chaos":
        return set_upchaos, apply_rule_chaos, args.x, args.n
    return None, None, None, None

def main(args):
    setup, apply, x, n = set_functions(args)
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Cellular Automata")
    done = False
    clock = pygame.time.Clock()
    cells = np.zeros((height_arr, width_arr), dtype=int)
    generation = 0
    screen.fill(WHITE)

    setup(screen, cells, x)
    while not done:
        cells = apply(screen, cells, n)
        pygame.display.update()
        if generation%10 == 0:
            print("{}{}".format("Generation indicator: g=", generation))
        generation += 1
        clock.tick(generationTimestep)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("{}{}".format("Generation indicator: g=", generation))
                done = True


if __name__ == "__main__":
    # create the top-level parser
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help="commands", dest="commands")

    # create the parser for the "gol" command
    parser_gol = subparsers.add_parser("gol")
    parser_gol.add_argument("-x", type=int, default=50, help="Set number for generation")

    # create the parser for the "neumann" command
    parser_neumann = subparsers.add_parser("neumann")

    parser_chaos = subparsers.add_parser("chaos")
    parser_chaos.add_argument("-x", type=int, default=50, help="Set number for generation")
    parser_chaos.add_argument("-n", type=int, default=3, help="Set number of neighbors")

    args = parser.parse_args()
    main(args)
    pygame.quit()
