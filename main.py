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
WIDTH = 1400
HEIGHT = 1400
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
    finish = pygame.image.load("images/finish.png")
    farleftcell = (GRID_SIDES_COUNT -1) * CELL_LENGTH
    finish = pygame.transform.scale(finish, (CELL_LENGTH -2, CELL_LENGTH -2))
    screen.blit(finish, (farleftcell, farleftcell))
    pygame.display.update()  

font = pygame.font.Font(None, 32)
input_grid_size = pygame.Rect(1 , WIDTH - 38, 140, 32)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
text = '{}'.format(GRID_SIDES_COUNT)

moves_count_label = pygame.Rect(150 , WIDTH - 38, 250, 32)



inititalise_maze()

moves = 0
moves_text = 'moves made : {}'.format(moves)

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
                moves = moves + 1
            if event.key == pygame.K_RIGHT:
                maze.TryMoveRight()
                moves = moves + 1
            if event.key == pygame.K_UP:
                maze.TryMoveUp()
                moves = moves + 1
            if event.key == pygame.K_DOWN:
                maze.TryMoveDown()
                moves = moves + 1
            if active:
                if event.key == pygame.K_RETURN:
                    screen.fill((30, 30, 30))
                    GRID_SIDES_COUNT = int(text)
                    inititalise_maze()
                    text = ''
                    moves = 0
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
            
            painter.fill_cell_small(maze.get_current_cell(), color=GREEN)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_grid_size.collidepoint(event.pos):
                active = not active
            else:
                active = False
            if active:
                text = ''
                color = color_active  
            else:
                color = color_inactive
           
        moves_text = 'moves made : {}'.format(moves)
        moves_txt_surface = font.render(moves_text, True, color)
        screen.fill((30, 30, 30), moves_count_label)
        screen.blit(moves_txt_surface, (moves_count_label.x+5, moves_count_label.y+5))
        pygame.draw.rect(screen, color, moves_count_label, 2)


        txt_surface = font.render(text, True, color)
        screen.fill((30, 30, 30), input_grid_size)        
        screen.blit(txt_surface, (input_grid_size.x+5, input_grid_size.y+5))
        # Blit the input_grid_size rect.
        pygame.draw.rect(screen, color, input_grid_size, 2)

        pygame.display.flip()