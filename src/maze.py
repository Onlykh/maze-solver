from cell import Cell
from window import Window
import time
from typing import Union
import random


# Numeric type that can be either int or float
Number = Union[int, float]


class Maze:
    def __init__(self, x1: Number,
                 y1: Number,
                 num_rows: int,
                 num_cols: int,
                 cell_size_x: Number, cell_size_y: Number, win=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            self.randomness = random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        self._solve_r()

    def _create_cells(self):
        self._cells = []
        for i in range(self._num_rows):
            self._cells.append([])
            for j in range(self._num_cols):
                self._cells[i].append(Cell(self._win))

        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        x1 = self._x1 + (j*self._cell_size_x)
        y1 = self._y1 + (i*self._cell_size_y)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        if self._win:
            self._cells[i][j].draw(x1, y1, x2, y2)
            self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        self._cells[len(self._cells)-1][len(self._cells[0]) -
                                        1].has_bottom_wall = False
        self._draw_cell(len(self._cells)-1, len(self._cells[0]) - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        # check possible roads
        possible_paths = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]

        while True:
            paths_to_visit = []
            for possible_path in possible_paths:
                if 0 <= possible_path[0] < len(self._cells) and 0 <= possible_path[1] < len(self._cells[0]) and not self._cells[possible_path[0]][possible_path[1]].visited:
                    paths_to_visit.append(possible_path)

            if not paths_to_visit:
                self._draw_cell(i, j)
                return
            chosen_cell = random.choice(paths_to_visit)
            # knock out walls between this cell and the next cell(s)
            # right
            if chosen_cell[0] == i + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i + 1][j].has_top_wall = False
            # left
            if chosen_cell[0] == i - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i - 1][j].has_bottom_wall = False
            # down
            if chosen_cell[1] == j + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i][j + 1].has_left_wall = False
            # up
            if chosen_cell[1] == j - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i][j - 1].has_right_wall = False

            self._break_walls_r(chosen_cell[0], chosen_cell[1])

    def _reset_cells_visited(self):
        for cell_row in self._cells:
            for cell in cell_row:
                cell.visited = False

    def _solve_r(self, i=0, j=0):
        self._animate()
        current_cell = self._cells[i][j]
        current_cell.visited = True
        if i == len(self._cells) - 1 and j == len(self._cells[0]) - 1:
            return True
        if 0 <= i-1 < len(self._cells) and not self._cells[i-1][j].visited and not current_cell.has_top_wall:
            current_cell.draw_move(self._cells[i-1][j])
            move = self._solve_r(i-1, j)
            if move:
                return True
            current_cell.draw_move(self._cells[i-1][j], True)
        if 0 <= i+1 < len(self._cells) and not self._cells[i+1][j].visited and not current_cell.has_bottom_wall:
            current_cell.draw_move(self._cells[i+1][j])
            move = self._solve_r(i+1, j)
            if move:
                return True
            current_cell.draw_move(self._cells[i+1][j], True)
        if 0 <= j-1 < len(self._cells[0]) and not self._cells[i][j-1].visited and not current_cell.has_left_wall:
            current_cell.draw_move(self._cells[i][j-1])
            move = self._solve_r(i, j-1)
            if move:
                return True
            current_cell.draw_move(self._cells[i][j-1], True)
        if 0 <= j+1 < len(self._cells[0]) and not self._cells[i][j+1].visited and not current_cell.has_right_wall:
            current_cell.draw_move(self._cells[i][j+1])
            move = self._solve_r(i, j+1)
            if move:
                return True
            current_cell.draw_move(self._cells[i][j+1], True)
        return False
