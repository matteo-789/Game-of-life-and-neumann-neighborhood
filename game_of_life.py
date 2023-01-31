import pygame
import numpy as np
from env import *

def set_upgol(screen, cells, ipg):
    for gene in range(height_arr):
        for _ in range(ipg):
            nb = rng.choice(int(width_arr), replace=False)
            pygame.draw.rect(screen, BLACK, [nb*cellSize, gene*cellSize, cellSize, cellSize])
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

def draw_glider(i, d, value, screen):
    if value == 1:
        pygame.draw.rect(screen, BLACK, [d*cellSize, cellSize*i, cellSize, cellSize])
    else:
        pygame.draw.rect(screen, WHITE, [d*cellSize, cellSize*i, cellSize, cellSize])


def apply_rule_gol(screen, cells, nb_neighb=None):
    new_cells = np.zeros((height_arr, width_arr), dtype=int)
    for i, row in enumerate(cells):
        for d, value in enumerate(row):
            count = 0
            if d == width_arr-1:
                count += row[d-1]
                count += row[0]
                if i == 0:
                    count += cells[height_arr-1][d]
                    count += cells[i+1][d]
                    count += cells[height_arr-1][0]
                    count += cells[i+1][0]
                    count += cells[height_arr-1][d-1]
                    count += cells[i+1][d-1]
                elif i == height_arr-1:
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
                count += row[width_arr-1]
                count += row[d+1]
                if i == 0:
                    count += cells[height_arr-1][d]
                    count += cells[i+1][d]
                    count += cells[height_arr-1][width_arr-1]
                    count += cells[i+1][width_arr-1]
                    count += cells[height_arr-1][d+1]
                    count += cells[i+1][d+1]
                elif i == height_arr-1:
                    count += cells[0][d]
                    count += cells[i-1][d]
                    count += cells[0][width_arr-1]
                    count += cells[i-1][width_arr-1]
                    count += cells[0][d+1]
                    count += cells[i-1][d+1]
                else:
                    count += cells[i-1][d]
                    count += cells[i+1][d]
                    count += cells[i-1][width_arr-1]
                    count += cells[i+1][width_arr-1]
                    count += cells[i-1][d+1]
                    count += cells[i+1][d+1]
            else:
                count += row[d-1]
                count += row[d+1]
                if i == 0:
                    count += cells[height_arr-1][d]
                    count += cells[i+1][d]
                    count += cells[height_arr-1][d-1]
                    count += cells[i+1][d-1]
                    count += cells[height_arr-1][d+1]
                    count += cells[i+1][d+1]
                elif i == height_arr-1:
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
            draw_glider(i,d,new_cells[i][d], screen)
    return new_cells
