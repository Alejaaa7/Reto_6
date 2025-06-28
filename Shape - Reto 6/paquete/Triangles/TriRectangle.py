# TriRectangle.py

from ..Shape.Point import Point
from ..Shape.Line import Line
from ..Shape.Shape import Shape
from ..Triangles.Triangles import Triangles

class TriRectangle(Triangles):
    def __init__(self, p1: Point, p2: Point, p3: Point):
        super().__init__(p1, p2, p3)
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

        # Validar que sea triángulo rectángulo:
        if not self.if_is_trirectangle():
            raise ValueError("Estos puntos NO forman un triángulo rectángulo.")
        
    def if_is_trirectangle(self):

        # Nuevamente validar que tiene tres lados:
        if len(self.edges) != 3:
            raise ValueError("Los triángulos deben tener 3 lados!")
            
        a = self.edges[0].length
        b = self.edges[1].length
        c = self.edges[2].length

        return a == (b ** 2 + c ** 2) ** 0.5 \
            or b == (a ** 2 + c ** 2) ** 0.5 \
            or c == (b ** 2 + a ** 2) ** 0.5