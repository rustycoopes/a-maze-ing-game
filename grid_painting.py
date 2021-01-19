from grid_creator import Grid, Cell, CellRelationships
from game_colors import WHITE, BLUE, RED, GREY

class CellPaintCoOrdinates():
    
    def __init__(self,cell1, cell2=None, cell_h=20, cell_w=20):
        self.Cell1 = cell1
        self.Cell2 = cell2
        self.Cell_h = cell_h
        self.Cell_w = cell_w
        self.TopLeft = None
        self.BottomLeft = None
        self.TopRight = None
        self.BottomRight = None
        self._calc_co_ordinates()
           

    def _calc_co_ordinates(self):

        minRow = self._get_min_row() - 1
        minCol = self._get_min_col() - 1
        maxRow = self._get_max_row() - 1
        maxCol = self._get_max_col() - 1

        self.TopLeft = [minRow * self.Cell_h, minCol * self.Cell_w]
        self.BottomLeft = [(maxRow + 1 )* self.Cell_h, minCol * self.Cell_w]
        self.TopRight = [minRow * self.Cell_h, (maxCol + 1) * self.Cell_w]
        self.BottomRight = [ (maxRow +1) * self.Cell_h, (maxCol + 1) * self.Cell_w]
        
        #cal co-ords - need width and height per cell
    def _get_min_row(self):
        if self.Cell2 is None:
            return self.Cell1.RowNum
        else:
            return min(self.Cell1.RowNum, self.Cell2.RowNum)

    def _get_min_col(self):
        if self.Cell2 is None:
            return self.Cell1.ColNum
        else:
            return min(self.Cell1.ColNum, self.Cell2.ColNum)

    def _get_max_row(self):
        if self.Cell2 is None:
            return self.Cell1.RowNum
        else:
            return max(self.Cell1.RowNum, self.Cell2.RowNum)

    def _get_max_col(self):
        if self.Cell2 is None:
            return self.Cell1.ColNum
        else:
            return max(self.Cell1.ColNum, self.Cell2.ColNum)

class GridPainter():

    def __init__(self, pygame, screen, cell_h, cell_w, top_left):
        self._pygame = pygame
        self._screen = screen
        self._cell_h = cell_h
        self._cell_w = cell_w
        self._top_left = top_left
        self._player_sprites = None

    def paint_grid(self, grid):

        cells = grid.get_cells()

        for cell in cells:
            self._paint_cell_outline(cell)

        self._pygame.display.update()  

    def set_player_sprites(self, player_sprites):
        self._player_sprites = player_sprites

    def fill_cell(self, cell1, cell2=None, color=BLUE):
        coOrds = CellPaintCoOrdinates(cell1, cell2, cell_h=self._cell_h, cell_w=self._cell_w)
        topleft_x = coOrds.TopLeft[1] +1
        topleft_y = coOrds.TopLeft[0] +1
        botright_x = coOrds.BottomRight[1] - topleft_x 
        botright_y = coOrds.BottomRight[0] - topleft_y 
        
        self._pygame.draw.rect(self._screen, color, (topleft_x, topleft_y, botright_x, botright_y), 0)        # used to re-colour the path after single_cell
        self._pygame.display.update()   

    def paint_player(self, cell, direction):
        coOrds = CellPaintCoOrdinates(cell, cell_h=self._cell_h, cell_w=self._cell_w)
        image = self._player_sprites[direction]
        margin = (coOrds.TopRight[1]-coOrds.TopLeft[1] ) // 4 
        self._screen.blit(image, (coOrds.TopLeft[1] + margin, coOrds.TopLeft[0] + margin))
        self._pygame.display.update()

    def set_finish(self, finish_image, farleftcell):
        self._screen.blit(finish_image, (farleftcell, farleftcell))
 

    def fill_cell_small(self, cell1, cell2=None, color=BLUE):
        coOrds = CellPaintCoOrdinates(cell1, cell2, cell_h=self._cell_h, cell_w=self._cell_w)
        margin = (coOrds.TopRight[1]-coOrds.TopLeft[1] ) // 2 
        topleft_x = coOrds.TopLeft[1] + (margin /2)
        topleft_x = coOrds.TopLeft[1] + (margin /2)
        topleft_y = coOrds.TopLeft[0] + (margin /2)
        botright_x =  margin
        botright_y =  margin
        
        self._pygame.draw.rect(self._screen, color, (topleft_x, topleft_y, botright_x, botright_y), 0)        # used to re-colour the path after single_cell
        self._pygame.display.update()   

    def fill_cell_circle_small(self, cell1, cell2=None, color=GREY):
        coOrds = CellPaintCoOrdinates(cell1, cell2, cell_h=self._cell_h, cell_w=self._cell_w)
        margin = (coOrds.TopRight[1]-coOrds.TopLeft[1] ) // 2 
        mid_x = coOrds.TopLeft[1] + margin
        mid_y = coOrds.TopLeft[0] + margin

        self._pygame.draw.circle(self._screen, color, (mid_x, mid_y ), margin / 8)        
        self._pygame.display.update()   



    def _paint_cell_outline(self, cell):
            coords = CellPaintCoOrdinates(cell, cell_h=self._cell_h, cell_w=self._cell_w)

            self._pygame.draw.line(self._screen, WHITE, coords.TopLeft, coords.TopRight)           # top of cell
            self._pygame.draw.line(self._screen, WHITE, coords.TopRight, coords.BottomRight)   # right of cell
            self._pygame.draw.line(self._screen, WHITE, coords.BottomLeft, coords.BottomRight)   # bottom of cell
            self._pygame.draw.line(self._screen, WHITE, coords.TopLeft, coords.BottomLeft)           # left of cell

