# Scalene.py

from ..Shape.Point import Point
from ..Shape.Line import Line
from ..Shape.Shape import Shape
from ..Triangles.Triangles import Triangles

class Scalene(Triangles):
    def __init__(self, p1, p2, p3):
        super().__init__(p1, p2, p3)
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

        # Validar primero si es escaleno:
        if not self.if_is_scalene():
            raise ValueError("Los puntos no forman un triángulo escaleno.")
        
    def is_is_scalente(self):
        
        # Validar que sí tenga tres lados:
        if len(self.edges) != 3:
            raise ValueError("Un triángulo debe tener tres lados!")
        
        # Ahora sí verificar que sea ESCALENO:

        a = self.edges[0].length
        b = self.edges[1].length
        c = self.edges[2].length

        return a != b  and b != c and c != a
