import pygame
import time
import random
import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
import grid_creator
from grid_painting import GridPainter
from maze_creator import Maze_Maker
from game_colors import RED, GREEN, BLUE
# set up pygame window
WIDTH = 600
HEIGHT = 600
FPS = 30



def pathcreated(cell1, cell2):
    time.sleep(0.005)
    painter.fill_cell(cell1, cell2)
    print("path from {} to {}".format(cell1.Number, cell2.Number))

def pathbacktracked(cell):
    painter.fill_cell(cell, color=RED)
    time.sleep(0.005)
    painter.fill_cell(cell)
    print("backtracking from {}".format(cell.Number))


# initalise Pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Maze Generator")
clock = pygame.time.Clock()

grid_start = [1,1]
GRID_SIDES_COUNT = 10
CELL_LENGTH = WIDTH // GRID_SIDES_COUNT

myGrid = grid_creator.Grid(CELL_LENGTH,CELL_LENGTH,GRID_SIDES_COUNT ,GRID_SIDES_COUNT,grid_start)

painter = GridPainter(pygame, screen,CELL_LENGTH,CELL_LENGTH)
painter.paint_grid(myGrid)

maze_gen = Maze_Maker(myGrid)
maze_gen.on_path_created(pathcreated)
maze_gen.on_back_track(pathbacktracked)
maze = maze_gen.create_new_maze()

painter.fill_cell(maze.get_current_cell(), color=GREEN)

x, y = CELL_LENGTH, CELL_LENGTH                     # starting position of grid
pygame.display.update()  
# ##### pygame loop #######
# ##### pygame loop #######
running = True
while running:
    # keep running at the at the right speed
    clock.tick(FPS)
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            painter.fill_cell(maze.get_current_cell(), color=BLUE)
            if event.key == pygame.K_LEFT:
                maze.TryMoveLeft()
            if event.key == pygame.K_RIGHT:
                maze.TryMoveRight()
            if event.key == pygame.K_UP:
                maze.TryMoveUp()
            if event.key == pygame.K_DOWN:
                maze.TryMoveDown()

            painter.fill_cell(maze.get_current_cell(), color=GREEN)
