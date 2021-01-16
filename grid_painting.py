from grid_creator import Grid, Cell, CellRelationships


class CellPaintCoOrdinates():
    def __init__(self, topleft, topright, bottomleft, bottomright):
        self.Topleft = topleft
        self.Topright = topright
        self.Bottomleft = bottomleft
        self.Bottomright = bottomright
        
class GridPainter():

    def __init__(self, pygame, screen):
        self._pygame = pygame
        self._screen = screen

    def paint_grid(self, grid):

        cells = grid.get_cells()
                #new_cell = Cell((i*j), [x,y], [x + self._cell_w, y], [x, y+ self._cell_h], [x + self._cell_w, y + self._cell_h])

#   generate line co-ordinates
#        self.Coordinates = CellPaintCoOrdinates(topleft, topright, bottomleft, bottomright)

        for cell in cells:
            self._paint_cell(cell)

        self._pygame.display.update()  


    def _paint_cell(self, cell):
            coords = cell.Coordinates

            self._pygame.draw.line(self._screen, WHITE, coords.Topleft, coords.Topright)           # top of cell
            self._pygame.draw.line(self._screen, WHITE, coords.Topright, coords._Bottomright)   # right of cell
            self._pygame.draw.line(self._screen, WHITE, coords.Bottomleft, coords.Bottomright)   # bottom of cell
            self._pygame.draw.line(self._screen, WHITE, coords.Topleft, coords.Bottomleft)           # left of cell

    def print_debug(self,grid):
        cells = grid.get_cells()

        for cell in cells:
            logging.info(cell.describe())




