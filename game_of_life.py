import pygame
from numpy.random import default_rng
import numpy as np

rng = default_rng()

def set_upgol(screen, cells, cellSize, larg_arr, long_arr, x):
    for gene in range(long_arr):
        for _ in range(x):
            nb = rng.choice(int(larg_arr), replace=False)
            pygame.draw.rect(screen, (0, 0, 0), [nb*cellSize, gene*cellSize, cellSize, cellSize])
            cells[gene][nb] = 1

def rule_gol(count, value):
    if value == 1 and count < 2:
        return 0
    elif value == 1 and (count == 2 or count == 3):
        return 1
    elif value == 1 and count > 3:
        return 0
    elif value == 0 and count == 3:
        return 1
    else:
        return value
    return 0

def draw_glider(i, d, value, screen, cellSize):
    if value == 1:
        pygame.draw.rect(screen, (0, 0, 0), [d*cellSize, cellSize*i, cellSize, cellSize])
    else:
        pygame.draw.rect(screen, (255, 255, 255), [d*cellSize, cellSize*i, cellSize, cellSize])


def apply_rule_gol(screen, cells, cellSize, larg_arr, long_arr):
    new_cells = np.zeros((long_arr, larg_arr), dtype=int)
    for i, row in enumerate(cells):
        for d, value in enumerate(row):
            count = 0
            if d == larg_arr-1:
                count += row[d-1]
                count += row[0]
                if i == 0:
                    count += cells[long_arr-1][d]
                    count += cells[i+1][d]
                    count += cells[long_arr-1][0]
                    count += cells[i+1][0]
                    count += cells[long_arr-1][d-1]
                    count += cells[i+1][d-1]
                elif i == long_arr-1:
                    count += cells[0][d]
                    count += cells[i-1][d]
                    count += cells[0][0]
                    count += cells[i-1][0]
                    count += cells[0][d-1]
                    count += cells[i-1][d-1]
                else:
                    count += cells[i-1][d]
                    count += cells[i+1][d]
                    count += cells[i-1][0]
                    count += cells[i+1][0]
                    count += cells[i-1][d-1]
                    count += cells[i+1][d-1]
            elif d == 0:
                count += row[larg_arr-1]
                count += row[d+1]
                if i == 0:
                    count += cells[long_arr-1][d]
                    count += cells[i+1][d]
                    count += cells[long_arr-1][larg_arr-1]
                    count += cells[i+1][larg_arr-1]
                    count += cells[long_arr-1][d+1]
                    count += cells[i+1][d+1]
                elif i == long_arr-1:
                    count += cells[0][d]
                    count += cells[i-1][d]
                    count += cells[0][larg_arr-1]
                    count += cells[i-1][larg_arr-1]
                    count += cells[0][d+1]
                    count += cells[i-1][d+1]
                else:
                    count += cells[i-1][d]
                    count += cells[i+1][d]
                    count += cells[i-1][larg_arr-1]
                    count += cells[i+1][larg_arr-1]
                    count += cells[i-1][d+1]
                    count += cells[i+1][d+1]
            else:
                count += row[d-1]
                count += row[d+1]
                if i == 0:
                    count += cells[long_arr-1][d]
                    count += cells[i+1][d]
                    count += cells[long_arr-1][d-1]
                    count += cells[i+1][d-1]
                    count += cells[long_arr-1][d+1]
                    count += cells[i+1][d+1]
                elif i == long_arr-1:
                    count += cells[0][d]
                    count += cells[i-1][d]
                    count += cells[0][d-1]
                    count += cells[i-1][d-1]
                    count += cells[0][d+1]
                    count += cells[i-1][d+1]
                else:
                    count += cells[i-1][d]
                    count += cells[i+1][d]
                    count += cells[i-1][d-1]
                    count += cells[i+1][d-1]
                    count += cells[i-1][d+1]
                    count += cells[i+1][d+1]
            new_cells[i][d] = rule_gol(count, cells[i][d])
            draw_glider(i,d,new_cells[i][d], screen, cellSize)
    return new_cells
