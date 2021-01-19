import pytest
from grid_painting import CellPaintCoOrdinates
from grid_creator import Cell


@pytest.fixture
def singleCell():
    cell1 = Cell(1,1,1)
    return cell1

@pytest.fixture
def singleMiddleCell():
    cell1 = Cell(2,3,1)
    return cell1

def test_cell_coordinatess(singleCell):
    coOrds = CellPaintCoOrdinates(singleCell, None, 10, 10)
    assert coOrds.TopLeft == [0,0]
    assert coOrds.TopRight == [0,10]
    assert coOrds.BottomLeft == [10,0]
    assert coOrds.BottomRight == [10,10]

def test_cell_coordinates_rectangle(singleCell):
    coOrds = CellPaintCoOrdinates(singleCell, None, 30, 20)
    assert coOrds.TopLeft == [0,0]
    assert coOrds.TopRight == [0,20]
    assert coOrds.BottomLeft == [30,0]
    assert coOrds.BottomRight == [30,20]

def test_cell_coordinatess_right(singleMiddleCell):
    coOrds = CellPaintCoOrdinates(singleMiddleCell, None, 10, 10)
    assert coOrds.TopLeft == [10,20]
    assert coOrds.TopRight == [10,30]
    assert coOrds.BottomLeft == [20,20]
    assert coOrds.BottomRight == [20,30]


def test_cell_coordinatess_twoCells(singleMiddleCell,singleCell):
    coOrds = CellPaintCoOrdinates(singleMiddleCell, singleCell, 10, 10)
    assert coOrds.TopLeft == [0,0]
    assert coOrds.TopRight == [0,30]
    assert coOrds.BottomLeft == [20,0]
    assert coOrds.BottomRight == [20,30]