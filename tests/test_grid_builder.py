import pytest
from grid_creator import Grid

def test_right_number_of_cells_and_rowcol(twobytwogrid):

    cells = twobytwogrid.get_cells()
    assert len(cells) == 4
    assert len(cells) == 4
    assert cells[0].RowNum == 1
    assert cells[0].ColNum == 1
    assert cells[1].RowNum == 2
    assert cells[1].ColNum == 1
    assert cells[2].RowNum == 1
    assert cells[2].ColNum == 2
    assert cells[3].RowNum == 2
    assert cells[3].ColNum == 2
"""
    1  3
    2  4
"""

def test_assert_lefts(twobytwogrid):
    cells = twobytwogrid.get_cells()
    assert cells[0].Neighbours.Left is None
    assert cells[1].Neighbours.Left is None
    assert cells[2].Neighbours.Left is cells[0]
    assert cells[3].Neighbours.Left is cells[1]

def test_assert_rights(twobytwogrid):
    cells = twobytwogrid.get_cells()
    assert cells[0].Neighbours.Right is cells[2]
    assert cells[1].Neighbours.Right is cells[3]
    assert cells[2].Neighbours.Right is None
    assert cells[3].Neighbours.Right is None

def test_assert_tops(twobytwogrid):
    cells = twobytwogrid.get_cells()
    assert cells[0].Neighbours.Above is None
    assert cells[1].Neighbours.Above is cells[0]
    assert cells[2].Neighbours.Above is None
    assert cells[3].Neighbours.Above is cells[2]


def test_assert_belows(twobytwogrid):
    cells = twobytwogrid.get_cells()
    assert cells[0].Neighbours.Below is cells[1]
    assert cells[1].Neighbours.Below is None
    assert cells[2].Neighbours.Below is cells[3]
    assert cells[3].Neighbours.Below is None


"""
    1  4  7
    2  5  8
    3  6  9
"""

def test_assert_middle(threebythreegrid):
    cells = threebythreegrid.get_cells()
    assert len(cells) == 9
    assert cells[4].Neighbours.Left is cells[1]
    assert cells[4].Neighbours.Right is cells[7]
    assert cells[4].Neighbours.Above is cells[3]
    assert cells[4].Neighbours.Below is cells[5]


    assert cells[8].Neighbours.Below is None
    assert cells[8].Neighbours.Right is None
    assert cells[8].Neighbours.Left is cells[5]
    assert cells[8].Neighbours.Above is cells[7]