import unittest
from maze import Maze


class Test(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )

    def test_maze_entry_brake(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        top_cell = m1._cells[0][0]
        self.assertEqual(
            False,
            top_cell.has_top_wall
        )
        top_cell = m1._cells[len(m1._cells)-1][len(m1._cells[0])-1]
        self.assertEqual(
            False,
            top_cell.has_bottom_wall
        )

    def test_cell_visit_reset(self):
        num_cols = 5
        num_rows = 5
        maze = Maze(5, 5, num_rows, num_cols, 50, 50)
        for cell_row in maze._cells:
            for cell in cell_row:
                self.assertEqual(
                    False,
                    cell.visited
                )


if __name__ == "__main__":
    unittest.main()
