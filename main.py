import pygame
import time
import random
import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
import grid_creator
from grid_painting import GridPainter
from maze_creator import Maze_Maker
from game_colors import RED, GREEN, BLUE, GREY
# set up pygame window
WIDTH = 1000
HEIGHT = 1000
FPS = 30

GRID_SIDES_COUNT = 5


def pathcreated(cell1, cell2):
    #time.sleep(0.005)
    painter.fill_cell(cell1, cell2)
    print("path from {} to {}".format(cell1.Number, cell2.Number))

def pathbacktracked(cell):
    painter.fill_cell(cell, color=RED)
    #time.sleep(0.005)
    painter.fill_cell(cell)
    print("backtracking from {}".format(cell.Number))


# initalise Pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Olivers A-Maze-ing Game")
clock = pygame.time.Clock()

grid_start = [40, 40]
painter = None
maze = None

def inititalise_maze():
    CELL_LENGTH = (WIDTH - grid_start[0]) // GRID_SIDES_COUNT
    global painter, maze
    myGrid = grid_creator.Grid(CELL_LENGTH,CELL_LENGTH,GRID_SIDES_COUNT ,GRID_SIDES_COUNT)

    painter = GridPainter(pygame, screen,CELL_LENGTH,CELL_LENGTH, grid_start)
    painter.paint_grid(myGrid)

    maze_gen = Maze_Maker(myGrid)
    maze_gen.on_path_created(pathcreated)
    maze_gen.on_back_track(pathbacktracked)
    maze = maze_gen.create_new_maze()

    painter.fill_cell_small(maze.get_current_cell(), color=GREEN)
    pygame.display.update()  

font = pygame.font.Font(None, 32)
input_box = pygame.Rect(1 , WIDTH - 38, 140, 32)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
text = '{}'.format(GRID_SIDES_COUNT)

inititalise_maze()

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
            painter.fill_cell_small(maze.get_current_cell(), color=BLUE)
            painter.fill_cell_circle_small(maze.get_current_cell(), color=GREY)
            if event.key == pygame.K_LEFT:
                maze.TryMoveLeft()
            if event.key == pygame.K_RIGHT:
                maze.TryMoveRight()
            if event.key == pygame.K_UP:
                maze.TryMoveUp()
            if event.key == pygame.K_DOWN:
                maze.TryMoveDown()
            if active:
                if event.key == pygame.K_RETURN:
                    screen.fill((30, 30, 30))
                    GRID_SIDES_COUNT = int(text)
                    inititalise_maze()
                    text = ''
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
            
            painter.fill_cell_small(maze.get_current_cell(), color=GREEN)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False
            if active:
                text = ''
                color = color_active  
            else:
                color = color_inactive
           

        screen.fill((30, 30, 30), input_box)
        
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()