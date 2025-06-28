# Square.py

from ..Shape.Point import Point
from ..Shape.Line import Line
from ..Shape.Shape import Shape
from ..Rectangle.Rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, p1: Point, p2: Point, p3: Point, p4: Point):
        super().__init__(p1, p2, p3, p4)
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

        # Primera verificación de que es un cuadrado:
        if not self.if_is_a_square:
            raise ValueError("Los puntos no forman un cuadrado.")
        
    def if_is_a_square(self):
        if all(i == self.edges[0].length for i in self.edges):
            return True
        else:
            return False