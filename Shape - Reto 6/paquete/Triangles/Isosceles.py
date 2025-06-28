# Isosceles.py

from ..Shape.Point import Point
from ..Shape.Line import Line
from ..Shape.Shape import Shape
from ..Triangles.Triangles import Triangles

class Isosceles(Triangles):
    def __init__(self, p1: Point, p2: Point, p3: Point):
        super().__init__(p1, p2, p3)
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

        # Validar que sí sea isosceles:
        if not self.if_is_isosceles():
            raise ValueError("Estos puntos no forman un triángulo isosceles.")
        
    def if_is_isosceles(self):
        
        # Validar que sí tenga tres lados antes de crear los a, b, c:
        if len(self.edges) != 3:
            raise ValueError("Un triángulo debe tener tres lados!")
        
        a = self.edges[0].length
        b = self.edges[1].length
        c = self.edges[2].length

        # Se corrige la parte que verifica que SOLO dos lados son iguales:
        return a == b and b != c or \
               b == c and c != a or \
               c == a and a != b 