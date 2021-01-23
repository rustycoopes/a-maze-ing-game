from game_colors import WHITE
import logging
grid = []


class Grid():
    """ Container of cells.  Creating an n x n matrix of connected, navigable objects 
    """
    def __init__(self, cell_h, cell_w, cells_across, cells_down):
        self._cell_h = cell_h
        self._cell_w = cell_w
        self._cells_across = cells_across
        self._cells = []
        self._cells_down = cells_down
        self._create_cells()
        logging.info('creating cells {}  for grid  {} rows, {} columns'.format(len(self._cells), cells_down, cells_across))
        logging.debug('creating relationships between cells')
        self._build_relationships()

    def _create_cells(self):
        """ Initialises a set of empty cell objects, disconnected from each other
        """
 
        cell_number = 1
        for col_idx in range(1, self._cells_across + 1):        
            for row_idx in range(1, self._cells_down + 1):
                cell = Cell(row_idx, col_idx, cell_number)
                self._cells.append(cell)           
                cell_number = cell_number + 1     

    def _build_relationships(self):
        """ Enriches cell objects to build relationships betweenthem.  If there is a valid neighbour to a cell 
            a bi-directional mapping should be made. 
        """
 
        for i in range(0, len(self._cells)):
            cell_idx = self._cell_left_idx(i)
            if cell_idx > -1:
                self._cells[i].Neighbours.Left = self._cells[cell_idx]
            cell_idx = self._cell_right_idx(i)
            if cell_idx > -1:
                self._cells[i].Neighbours.Right = self._cells[cell_idx]
            cell_idx = self._cell_above_idx(i)
            if cell_idx > -1:
                self._cells[i].Neighbours.Above = self._cells[cell_idx]
            cell_idx = self._cell_below_idx(i)
            if cell_idx > -1:
                self._cells[i].Neighbours.Below = self._cells[cell_idx]

    def _cell_left_idx(self, i):
        return max(i - self._cells_down , -1)

    def _cell_right_idx(self, i):
        if self._cells[i].ColNum < self._cells_across:
            return i + + self._cells_down
        else:
            return -1

    def _cell_above_idx(self, i):
        if self._cells[i].RowNum > 1:
            return i - 1
        else: 
            return -1

    def _cell_below_idx(self, i):
        if self._cells[i].RowNum < self._cells_down:
            return i + 1
        else:
            return -1
        
    def get_cells(self):
        """ 
        Returns all cells, fully related. 
        """
        return self._cells

    def get_start_cell(self):
        return self._cells[0]

    def get_finish_cell(self):
        return self._cells[len(self._cells)-1]

class CellRelationships():
    """ 
    Structure to represent how to navigate between cells. 
    """

    def __init__(self):
        self.Above = None
        self.Below = None
        self.Left = None
        self.Right = None


class Cell():
    
    """ 
    Structure to represent a cell, with connected cells.. 
    """
    def __init__(self, row_num, col_num, number):
        self.RowNum = row_num
        self.ColNum = col_num
        self.Number = number
        self.Neighbours = CellRelationships()

    def describe(self):
        description = ['#:{}'.format(self.Number)]
        if self.Neighbours.Above is not None:
            description.append("Above is {} ".format(self.Neighbours.Above.Name))
        if self.Neighbours.Below is not None:
            description.append("Below is {} ".format(self.Neighbours.Below.Name))
        if self.Neighbours.Left is not None:
            description.append("Left is {} ".format(self.Neighbours.Left.Name))
        if self.Neighbours.Right is not None:
            description.append("Right is {} ".format(self.Neighbours.Right.Name))
        return ' '.join(description)

