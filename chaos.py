import pygame
import numpy as np
from env import *

def set_upchaos(screen, cells, ipg):
    for i, color in enumerate(RGB):
        for gene in range(height_arr):
            for _ in range(ipg):
                nb = rng.choice(int(width_arr), replace=False)
                pygame.draw.rect(screen, color, [nb*cellSize, gene*cellSize, cellSize, cellSize])
                cells[gene][nb] = i

def rule_chaos_neighb(count):
    if count == 1:
        return 1
    elif count == 2:
        return 2
    elif count == 3:
        return 3
    else:
        return 0

def draw_chaos_neighb(i, d, value, screen):
    if value == 1:
        pygame.draw.rect(screen, BLUE, [d*cellSize, cellSize*i, cellSize, cellSize])
    elif value == 2:
        pygame.draw.rect(screen, RED, [d*cellSize, cellSize*i, cellSize, cellSize])
    elif value == 3:
        pygame.draw.rect(screen, GREEN, [d*cellSize, cellSize*i, cellSize, cellSize])
    else:
        pygame.draw.rect(screen, WHITE, [d*cellSize, cellSize*i, cellSize, cellSize])

def apply_rule_chaos(screen, cells, nb_neighb):
    new_cells = np.zeros((height_arr, width_arr), dtype=int)
    for i, row in enumerate(cells):
        for d, value in enumerate(row):
            count = 0
            for n in range(nb_neighb):
                width_rdn = rdn.choice(int(width_arr), replace=True)
                height_rdn = rdn.choice(int(height_arr), replace=True)
                count += cells[height_rdn][width_rdn]
            new_cells[i][d] = rule_chaos_neighb(count)
            draw_chaos_neighb(i, d, new_cells[i][d], screen)
    return new_cells
