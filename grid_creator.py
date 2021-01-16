from game_colors import WHITE
import logging
grid = []


class Grid():

    def __init__(self, cell_h, cell_w, cells_across, cells_down, top_left):
        self._cell_h = cell_h
        self._cell_w = cell_w
        self._cells_across = cells_across
        self._cells = []
        self._cells_down = cells_down
        self._top_left = top_left
        self._create_cells()
        self._build_relationships()

    def _create_cells(self):
        for col_idx in range(1, self._cells_across + 1):        
            for row_idx in range(1, self._cells_down + 1):
                cell = Cell(row_idx, col_idx)
                self._cells.append(cell)                                           
    def _build_relationships(self):
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
        return self._cells

    def get_start_cell(self):
        return self._cells[0]


class CellRelationships():

    def __init__(self):
        self.Above = None
        self.Below = None
        self.Left = None
        self.Right = None


class Cell():
    
    def __init__(self, row_num, col_num):
        self.RowNum = row_num
        self.ColNum = col_num
        self.Number = row_num * col_num
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

