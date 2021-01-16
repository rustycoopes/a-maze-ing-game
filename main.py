import pygame
import time
import random
import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
import grid_creator

# set up pygame window
WIDTH = 500
HEIGHT = 600
FPS = 30
CELL_LENGTH = 20


# initalise Pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Maze Generator")
clock = pygame.time.Clock()

grid_start = [20,20]

myGrid = grid_creator.Grid(CELL_LENGTH,CELL_LENGTH, 2,2,grid_start)
painter = grid_creator.GridPainter(pygame, screen)
painter.paint_grid(myGrid)
painter.print_debug(myGrid)

x, y = CELL_LENGTH, CELL_LENGTH                     # starting position of grid
pygame.display.update()  
# ##### pygame loop #######
running = True
while running:
    # keep running at the at the right speed
    clock.tick(FPS)
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False
