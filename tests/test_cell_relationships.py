import pytest
from grid_creator import Cell


@pytest.fixture
def related_cells():
    cell1 = Cell(1,1,1)
    cell2 = Cell(2,2,1)
    cell3 = Cell(3, 1, 2)

    cell1.Neighbours.Right = cell3
    cell3.Neighbours.Left = cell1
    
    cell1.Neighbours.Below = cell2
    cell2.Neighbours.Above = cell1
    return cell1
 

 
def test_cantest_relationships_right(related_cells):
    assert related_cells.Neighbours.Right.Neighbours.Left is related_cells

def test_cantest_relationships_below(related_cells):
    assert related_cells.Neighbours.Below.Neighbours.Above is related_cells
