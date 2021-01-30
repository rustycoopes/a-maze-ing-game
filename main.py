
import pygame
import time
import random
import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
import grid_creator
from grid_painting import GridPainter
from maze_creator import Maze_Maker
from game_colors import RED, GREEN, BLUE, GREY, INACTIVE, ACTIVE
import grid_images
from maze_solver import Solver

import ctypes
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

logging.info("Detected screem size as {}".format(screensize))

min_screen_size = int(min(screensize) * .95)

WIDTH = min_screen_size
HEIGHT = min_screen_size
FPS = 30
GRID_SIDES_COUNT = 5




# initalise Pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Olivers A-Maze-ing Game")
clock = pygame.time.Clock()

grid_start = [0, 0]

# CREATE GAME STATE OJECT
painter = None
maze_cursor = None
grid_size_input_text = ''
move_count = 0
solution_path = None
finish_cell = None
solution_button_text = 'Show solution'

def pathcreated(cell1, cell2):
    """ paint a maze path ! """
    painter.fill_cell(cell1, cell2)

def pathbacktracked(cell):
    """ call back to reversing the path"""
    painter.fill_cell(cell, color=RED)
    painter.fill_cell(cell)


def inititalise_maze():
    """ Create the maze game:
        * Paint a grid
        * Calculate a random maze
        * Paint the maze
        * Set the player and finish location on screen
    """
    CELL_LENGTH = (WIDTH - grid_start[0]) // GRID_SIDES_COUNT
    global painter, maze_cursor, grid_size_input_text, move_count, solution_path, finish_cell, solution_button_text
    blank_grid = grid_creator.Grid(CELL_LENGTH,CELL_LENGTH,GRID_SIDES_COUNT ,GRID_SIDES_COUNT)

    painter = GridPainter(pygame, screen,CELL_LENGTH,CELL_LENGTH, grid_start)
    painter._clear_screen() 
    painter.paint_grid(blank_grid)

    maze_gen = Maze_Maker(blank_grid)
    maze_gen.on_path_created(pathcreated)
    maze_gen.on_back_track(pathbacktracked)
    maze_cursor = maze_gen.create_new_maze()
    finish_cell = blank_grid.get_finish_cell()
    maze_solver = Solver(blank_grid.get_finish_cell())
    
    if GRID_SIDES_COUNT < 30:  # Recusive depth error avoidance... the try catch is not working -  i want to keep recursion to display issue
        solution_exists = maze_solver.create_solution(maze_cursor)
        solution_path = maze_solver.get_maze_solution()
    else:
        solution_exists = False

    
    logging.info("Solution found : {}".format(solution_exists))
    if solution_exists:
        logging.info("Solution contains {} steps".format(len(solution_path)))
        solution_button_text = 'Show solution'
    else:
        solution_button_text = 'NO solution'
    painter.set_finish(grid_images.create_finish(CELL_LENGTH), ((GRID_SIDES_COUNT -1) * CELL_LENGTH))
    painter.set_player_sprites(grid_images.create_sprites(CELL_LENGTH))
    painter.paint_player(maze_cursor.get_current_cell(), pygame.K_DOWN)
    grid_size_input_text = ''
    move_count = 0
    pygame.display.update()  


grid_size_input_text = '{}'.format(GRID_SIDES_COUNT)
input_grid_size_rect = pygame.Rect(1 , WIDTH - 38, 140, 32)
moves_count_label_rect = pygame.Rect(150 , WIDTH - 38, 250, 32)
show_solution_button_rect = pygame.Rect(410 , WIDTH - 38, 200, 32)
maze_completed_rect = pygame.Rect(410 , WIDTH - 38, 200, 32)


input_grid_size_is_active = False



def _action_mouse_click_on_grid_size_setting(event):
    """ Handle the capture of mouse clicking to start capturing (or clearing) the grid size  """
    global input_grid_size_is_active, grid_size_input_text
    if input_grid_size_rect.collidepoint(event.pos):
        input_grid_size_is_active = not input_grid_size_is_active
    else:
        input_grid_size_is_active = False
    if input_grid_size_is_active:
        grid_size_input_text = ''

def _action_mouse_click_on_show_solution(event):
    """ Handle the capture of mouse clicking to show the solution path  """
    global solution_button_text
    if show_solution_button_rect.collidepoint(event.pos):
        if solution_button_text == 'Show solution':
            solution_button_text = 'Hide solution'
            painter.paint_solution(solution_path)
        else:
            solution_button_text = 'Show solution'
            painter.unpaint_solution(solution_path)

def _action_mouse_click_on_maze_completed(event):
    """ Handle the capture of mouse clicking the complete message """
    if maze_completed_rect is not None and maze_completed_rect.collidepoint(event.pos):
        inititalise_maze()

def _maze_completed_congratulate_player():
    global maze_completed_rect
    message_height = 50
    message_width = 550
    message_top_left_y = (WIDTH - message_width) / 2
    message_top_left_x = (HEIGHT - message_height) / 2
    maze_completed_rect = pygame.Rect(message_top_left_y ,message_top_left_x, message_width, message_height)
    painter.update_rect_text("You did it ! great job Oliver  !!!!!, Click to restart", maze_completed_rect, input_grid_size_is_active)



def  _update_moves_label():
    moves_text = 'moves made : {}'.format(move_count)
    painter.update_rect_text(moves_text, moves_count_label_rect, input_grid_size_is_active)

def _update_grid_size_label():
    painter.update_rect_text(grid_size_input_text, input_grid_size_rect, input_grid_size_is_active)

def  _update_show_solution_button():
    painter.update_rect_text(solution_button_text, show_solution_button_rect, input_grid_size_is_active)



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
            painter.fill_cell(maze_cursor.get_current_cell(), color=BLUE)
            painter.fill_cell_circle_small(maze_cursor.get_current_cell(), color=GREY)
            if event.key == pygame.K_LEFT:
                maze_cursor.TryMoveLeft()
                move_count = move_count + 1
                painter.paint_player(maze_cursor.get_current_cell(), pygame.K_LEFT)
            if event.key == pygame.K_RIGHT:
                maze_cursor.TryMoveRight()
                painter.paint_player(maze_cursor.get_current_cell(), pygame.K_RIGHT)
                move_count = move_count + 1
            if event.key == pygame.K_UP:
                maze_cursor.TryMoveUp()
                painter.paint_player(maze_cursor.get_current_cell(), pygame.K_UP)
                move_count = move_count + 1
            if event.key == pygame.K_DOWN:
                maze_cursor.TryMoveDown()
                painter.paint_player(maze_cursor.get_current_cell(), pygame.K_DOWN)
                move_count = move_count + 1
            if input_grid_size_is_active:
                if event.key == pygame.K_RETURN:
                    GRID_SIDES_COUNT = int(grid_size_input_text)
                    inititalise_maze()

                elif event.key == pygame.K_BACKSPACE:
                    grid_size_input_text = grid_size_input_text[:-1]
                else:
                    grid_size_input_text += event.unicode
            

        if event.type == pygame.MOUSEBUTTONDOWN:
            _action_mouse_click_on_grid_size_setting(event)
            _action_mouse_click_on_show_solution(event)
            if maze_cursor.reached_finish():
                _action_mouse_click_on_maze_completed(event)

        if maze_cursor.reached_finish():
            _maze_completed_congratulate_player()

        _update_moves_label()
        _update_grid_size_label()
        _update_show_solution_button()



        pygame.display.flip()