from window import Window
from point import Point
from line import Line


class Cell:
    def __init__(self,  win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self.__win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            left_line_point1 = Point(self._x1, self._y1)
            left_line_point2 = Point(self._x1, self._y2)
            left_line = Line(left_line_point1, left_line_point2)
            self.__win.draw_line(left_line, "black")
        else:
            left_line_point1 = Point(self._x1, self._y1)
            left_line_point2 = Point(self._x1, self._y2)
            left_line = Line(left_line_point1, left_line_point2)
            self.__win.draw_line(left_line, "white")

        if self.has_right_wall:
            right_line_point1 = Point(self._x2, self._y1)
            right_line_point2 = Point(self._x2, self._y2)
            right_line = Line(right_line_point1, right_line_point2)
            self.__win.draw_line(right_line, "black")
        else:
            right_line_point1 = Point(self._x2, self._y1)
            right_line_point2 = Point(self._x2, self._y2)
            right_line = Line(right_line_point1, right_line_point2)
            self.__win.draw_line(right_line, "white")

        if self.has_top_wall:
            top_line_point1 = Point(self._x1, self._y1)
            top_line_point2 = Point(self._x2, self._y1)
            top_line = Line(top_line_point1, top_line_point2)
            self.__win.draw_line(top_line, "black")
        else:
            top_line_point1 = Point(self._x1, self._y1)
            top_line_point2 = Point(self._x2, self._y1)
            top_line = Line(top_line_point1, top_line_point2)
            self.__win.draw_line(top_line, "white")

        if self.has_bottom_wall:
            bottom_line_point1 = Point(self._x1, self._y2)
            bottom_line_point2 = Point(self._x2, self._y2)
            bottom_line = Line(bottom_line_point1, bottom_line_point2)
            self.__win.draw_line(bottom_line, "black")
        else:
            bottom_line_point1 = Point(self._x1, self._y2)
            bottom_line_point2 = Point(self._x2, self._y2)
            bottom_line = Line(bottom_line_point1, bottom_line_point2)
            self.__win.draw_line(bottom_line, "white")

    def get_center_x(self):
        return self._x1+(self._x2-self._x1)/2

    def get_center_y(self):
        return self._y1+(self._y2-self._y1)/2

    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo:
            color = "white"
        cell1_center = Point(self.get_center_x(), self.get_center_y())
        # print(self.get_center_x)
        cell2_center = Point(to_cell.get_center_x(), to_cell.get_center_y())
        # print(self.get_center_y)
        line = Line(cell1_center, cell2_center)
        self.__win.draw_line(line, color)
