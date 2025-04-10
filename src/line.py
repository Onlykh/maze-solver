from tkinter import Canvas
from point import Point
from typing import Final


class Line:
    __WIDTH: Final[int] = 2

    def __init__(self, point_1: Point, point_2: Point):
        self.point_1 = point_1
        self.point_2 = point_2

    def draw(self, canvas: Canvas, fill_color: str) -> None:
        canvas.create_line(
            self.point_1.x,
            self.point_1.y,
            self.point_2.x,
            self.point_2.y,
            fill=fill_color,
            width=Line.__WIDTH
        )
