import pytest
from maze_creator import MazeCursor
from grid_creator import Cell


@pytest.fixture
def two_step_path():
    cell1 = Cell(1,1,1)
    cell2 = Cell(1,2,2)
    cell3 = Cell(2, 1, 3)

    cell1.Neighbours.Right = cell3
    cell3.Neighbours.Left = cell1

    cell1.Neighbours.Below = cell2
    cell2.Neighbours.Above = cell1
 
    path = {}
    path[cell1] = [cell2, cell3]
    path[cell2] = [cell1]
    path[cell3] = [cell1]

    return MazeCursor(path, cell1)
    

def test_cursor_moves_right_then_left(two_step_path):
    cell1 = two_step_path.get_current_cell()
    two_step_path.TryMoveRight()
    cellToRight = two_step_path.get_current_cell()
    assert cell1.Neighbours.Right is cellToRight
    two_step_path.TryMoveLeft()
    assert two_step_path.get_current_cell() is cell1

def test_move_to_invalid_direction_doesnt_chang_current_cell(two_step_path):
    cell1 = two_step_path.get_current_cell()
    two_step_path.TryMoveUp()
    assert two_step_path.get_current_cell() is cell1
    two_step_path.TryMoveLeft()
    assert two_step_path.get_current_cell() is cell1

def test_cursor_moves_down_then_up(two_step_path):
    cell1 = two_step_path.get_current_cell()
    two_step_path.TryMoveDown()
    cellBelow = two_step_path.get_current_cell()
    assert cell1.Neighbours.Below is cellBelow
    two_step_path.TryMoveUp()
    assert two_step_path.get_current_cell() is cell1
