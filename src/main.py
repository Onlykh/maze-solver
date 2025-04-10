from window import Window
from maze import Maze


def main():
    win = Window(800, 600)
    num_cols = 15
    num_rows = 10
    Maze(20, 20, num_rows, num_cols, 50, 50, win)
    win.wait_for_close()


main()
