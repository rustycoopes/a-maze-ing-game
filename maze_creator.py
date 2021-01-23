import random
import logging

class MazeCursor():
    """ Represents a stateful location on the maze, with the ability to progress to 
    other connected cells.
    """
    def __init__(self, path, startCell):
        self._path = path
        self._start_cell = startCell
        self._curr_cell = startCell

    def reset_to_start(self):
        self._curr_cell = self._start_cell

    def reset_current_to_cell(self, cell):
        self._curr_cell = cell

    def get_current_cell(self):
        return self._curr_cell
        
    def TryMoveLeft(self):
        if  self._path[self._curr_cell] is None:
            return False
        can_move = self._curr_cell.Neighbours.Left in self._path[self._curr_cell]
        if can_move:
            self._curr_cell = self._curr_cell.Neighbours.Left
        return can_move

    def TryMoveRight(self):
        if  self._path[self._curr_cell] is None:
            return False
        can_move = self._curr_cell.Neighbours.Right in self._path[self._curr_cell]
        if can_move:
            self._curr_cell = self._curr_cell.Neighbours.Right  
        return can_move

    def TryMoveUp(self):
        if  self._path[self._curr_cell] is None:
            return False
        can_move = self._curr_cell.Neighbours.Above in self._path[self._curr_cell]
        if can_move:
            self._curr_cell = self._curr_cell.Neighbours.Above  
        return can_move

    def TryMoveDown(self):
        if  self._path[self._curr_cell] is None:
            return False
        can_move = self._curr_cell.Neighbours.Below in self._path[self._curr_cell]
        if can_move:
            self._curr_cell = self._curr_cell.Neighbours.Below  
        return can_move
class Maze_Maker():

    def __init__(self, grid):
        self._grid = grid
        self._visited = []
        self._stack = []
        self._maze_path ={}
        self._path_created_callback = None
        self._on_backtrack_callback = None
    
    def create_new_maze(self):
        """ Creates a new, unique maze path..
        Uses a backtracking algorithum to randomly move to neighboring cells, 
        carving a path of connections (and disconnections)
        the stack and visited collections are used to track where we have been, and 
        backtrack into other routes
        """
        logging.info("creating new maze creation")
        cell = self._grid.get_start_cell()
        self._visited.append(cell)
        self._stack.append(cell)

        while len(self._stack) > 0:
            cell = self._stack.pop()

            neighbour = self._get_unvisited_neighbour(cell)
            if neighbour is not None:
                logging.debug("creating path between cells {} and {}".format(cell.Number, neighbour.Number))
                self._stack.append(cell)
                self._make_path_between(cell, neighbour)
                self._stack.append(neighbour)
                self._visited.append(neighbour)
            else:
                if self._on_backtrack_callback is not None:
                    self._on_backtrack_callback(cell)
                logging.debug("back tracking from {}".format(cell.Number))


        return MazeCursor(self._maze_path, self._grid.get_start_cell())

    def on_path_created(self, callback):
        self._path_created_callback = callback

    def on_back_track(self, callback):
        self._on_backtrack_callback = callback

    def _get_unvisited_neighbour(self, cell):
        """ Return a random, unvisited neighbour.
        """
        unvisited = []
        if cell.Neighbours.Above is not None and cell.Neighbours.Above not in self._visited:
            unvisited.append(cell.Neighbours.Above)
        if cell.Neighbours.Below is not None and cell.Neighbours.Below not in self._visited:
            unvisited.append(cell.Neighbours.Below)
        if cell.Neighbours.Left is not None and cell.Neighbours.Left not in self._visited:
            unvisited.append(cell.Neighbours.Left)
        if cell.Neighbours.Right is not None and cell.Neighbours.Right not in self._visited:
            unvisited.append(cell.Neighbours.Right)
        if len(unvisited) == 0:
            return None
        return random.choice(unvisited)
    
    def _make_path_between(self, cell_from, cell_to):
        """ Creates a bi-direction path between cells.
        This is required for moving the player between cells.(walking back, not just fwd.)
        """
        if cell_from in self._maze_path:
            self._maze_path[cell_from].append(cell_to)
        else:
            self._maze_path[cell_from] = [cell_to]
        if cell_to in self._maze_path:
            self._maze_path[cell_to].append(cell_from)
        else:
            self._maze_path[cell_to] = [cell_from]


        if self._path_created_callback is not None:
            self._path_created_callback(cell_from, cell_to)




                                