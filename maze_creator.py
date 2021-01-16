import random


class maze_maker():


    def __init__(self, grid):
        self._grid = grid
        self._visited = []
        self._stack = []
    
    def create_new_maze(self):

            cell = self._grid.get_start_cell():
            self._visited.append(cell)
            self._stack.append(cell)

            while self._stack.count() > 0:
                cell = self._stack.pop(cell)
                neighbour = self._get_unvisited_neighbour(cell)
                if neighbour is not None:
                    self._stack.append(cell)
                    self._make_path_between(cell, neighbour)
                    self.stack.append(neighbour)
                    self._visited.append(neighbour)


    def _get_unvisited_neighbour(self, cell):
        pass
    
    def _make_path_between(self, cell1, cell2):
        pass
                                