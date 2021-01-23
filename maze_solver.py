import random
import logging
from maze_creator import MazeCursor


class Solver():

    def __init__(self,maze_finish):
        self._visited = []
        self._maze_finish = maze_finish
        self._maze_path =[]
        return
    

    def create_solution(self, cursor):
        """ Creates a maze path from current cursor to the finish.  The returns true if a path is found, false if not the.
        NOTE unlike rest of the game, this solution is recusive, adn highlights why NOT to use recursion, as depth errors
        are encountered easily
        """

        self._visited = [cursor.get_current_cell()]

        try:
            solved = self._recursive_solve(cursor)
        except RecursionError as re:
            logging.warning("No solution found due to recusion limit - this is why we use iterative !!!")
            solved = False

        self._log_solution()
        cursor.reset_to_start()
        return solved
        
    def _log_solution(self):
        for c in self._maze_path:
            logging.info("{}->".format(c.Number))

    def get_maze_solution(self):
        return self._maze_path
    
    def _recursive_solve(self, cursor):
        pre_move_cell = cursor.get_current_cell()
        logging.info("Starting recursion on curr cell {}->".format(pre_move_cell.Number))
        if(pre_move_cell == self._maze_finish):
            logging.info("Found end at cell {}".format(pre_move_cell.Number))
            return True
        else:

            while self._random_move_to_unvisited_neighbour(cursor):
                post_move_cell = cursor.get_current_cell()         
                logging.info("Found unvisited neighbor {}".format(post_move_cell.Number))
           
                self._visited.append(post_move_cell)

                if self._recursive_solve(cursor):
                    logging.info("Found solution in recursion adding cell to solution path {}".format(post_move_cell.Number))
                    self._maze_path.append(pre_move_cell)
                    return True
                else:
                    logging.info("subsequent recursion didnt solve, resetting cursor to {}".format(pre_move_cell.Number))
                    cursor.reset_current_to_cell(pre_move_cell)
            
            return False

    
    def _random_move_to_unvisited_neighbour(self, cursor):
        
        if self._move_or_revert(MazeCursor.TryMoveLeft, MazeCursor.TryMoveRight, cursor):
            return True
        elif self._move_or_revert(MazeCursor.TryMoveRight, MazeCursor.TryMoveLeft, cursor):
            return True
        elif self._move_or_revert(MazeCursor.TryMoveUp, MazeCursor.TryMoveDown, cursor):
            return True
        elif self._move_or_revert(MazeCursor.TryMoveDown, MazeCursor.TryMoveUp, cursor):
            return True
        else:
            return False

    def _move_or_revert(self, func_forward, func_backward, cursor):
        
        if func_forward(cursor):
            if cursor.get_current_cell() in self._visited:
               func_backward(cursor)  # returns false.
            else:
                return True

        return False
