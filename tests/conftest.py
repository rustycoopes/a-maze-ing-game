from grid_creator import Grid

import pytest
from configparser import ConfigParser


@pytest.fixture
def twobytwogrid():
    grid = Grid(10,10,2,2,[10,10])
    yield grid


@pytest.fixture
def threebythreegrid():
    grid = Grid(10,10,3,3,[10,10])
    yield grid
