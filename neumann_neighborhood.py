import pygame
import numpy as np
from env import *

def set_neumann_neighb(screen, cells, ipg=None):
    pygame.draw.rect(screen, BLACK, [int(width_arr/2)*cellSize, int(height_arr/2)*cellSize, cellSize, cellSize])
    cells[int(height_arr/2)][int(width_arr/2)] = 1

def rule_neumann_neighb(count):
    if count == 1:
        return 1
    elif count == 2:
        return 2
    elif count == 3:
        return 3
    else:
        return 0

def draw_neumann_neighb(i, d, value, screen):
    if value == 1:
        pygame.draw.rect(screen, BLACK, [d*cellSize, cellSize*i, cellSize, cellSize])
    elif value == 2:
        pygame.draw.rect(screen, RED, [d*cellSize, cellSize*i, cellSize, cellSize])
    elif value == 3:
        pygame.draw.rect(screen, GREEN, [d*cellSize, cellSize*i, cellSize, cellSize])
    elif value > 3:
        pygame.draw.rect(screen, WHITE, [d*cellSize, cellSize*i, cellSize, cellSize])

def get_updown(i, d, cells):
    count = 0
    if i == 0:
        count += cells[height_arr-1][d]
        count += cells[i+1][d]
    elif i == height_arr-1:
        count += cells[0][d]
        count += cells[i-1][d]
    else:
        count += cells[i-1][d]
        count += cells[i+1][d]
    return count

def apply_rule_neumann(screen, cells, nb_neighb=None):
    new_cells = np.zeros((height_arr, width_arr), dtype=int)
    for i, row in enumerate(cells):
        for d, value in enumerate(row):
            count = 0
            count = get_updown(i, d, cells)
            if d == width_arr-1:
                count += row[d-1]
                count += row[0]
            elif d == 0:
                count += row[width_arr-1]
                count += row[d+1]
            else:
                count += row[d-1]
                count += row[d+1]
            new_cells[i][d] = rule_neumann_neighb(count)
            draw_neumann_neighb(i,d,new_cells[i][d], screen)
    return new_cells
