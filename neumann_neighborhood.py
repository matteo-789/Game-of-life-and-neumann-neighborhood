import pygame
import numpy as np

def set_neumann_neighb(screen, cells, cellSize, larg_arr, long_arr):
    pygame.draw.rect(screen, (0, 0, 0), [int(larg_arr/2)*cellSize, int(long_arr/2)*cellSize, cellSize, cellSize])
    cells[int(long_arr/2)][int(larg_arr/2)] = 1

def rule_neumann_neighb(count):
    if count == 1:
        return 1
    else:
        return 0

def draw_neumann_neighb(i, d, value, screen, cellSize):
    if value == 1:
        pygame.draw.rect(screen, (0, 0, 0), [d*cellSize, cellSize*i, cellSize, cellSize])
    elif value < 1 or value > 1:
        pygame.draw.rect(screen, (255, 255, 255), [d*cellSize, cellSize*i, cellSize, cellSize])

def get_updown(i, d, cells, larg_arr, long_arr):
    count = 0
    if i == 0:
        count += cells[long_arr-1][d]
        count += cells[i+1][d]
    elif i == long_arr-1:
        count += cells[0][d]
        count += cells[i-1][d]
    else:
        count += cells[i-1][d]
        count += cells[i+1][d]
    return count

def apply_rule_neumann(screen, cells, cellSize, larg_arr, long_arr):
    new_cells = np.zeros((long_arr, larg_arr), dtype=int)
    for i, row in enumerate(cells):
        for d, value in enumerate(row):
            count = 0
            count = get_updown(i, d, cells, larg_arr, long_arr)
            if d == larg_arr-1:
                count += row[d-1]
                count += row[0]
            elif d == 0:
                count += row[larg_arr-1]
                count += row[d+1]
            else:
                count += row[d-1]
                count += row[d+1]
            new_cells[i][d] = rule_neumann_neighb(count)
            draw_neumann_neighb(i,d,new_cells[i][d], screen, cellSize)
    return new_cells
