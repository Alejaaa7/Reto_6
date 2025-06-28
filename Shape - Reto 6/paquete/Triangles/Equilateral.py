from ..Shape.Point import Point
from ..Shape.Line import Line
from ..Shape.Shape import Shape
from ..Triangles.Triangles import Triangles

class Equilateral(Triangles):
    def __init__(self, p1: Point, p2: Point, p3: Point):
        super().__init__(p1, p2, p3)
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

        # Validar si efectivamente sí es equilatero:
        if not self.if_is_equilateral:
            return ValueError("Estos puntos no forman un triángulo equilátero.")

        def if_is_equilateral(self):

        # Validar que existan tres lados:
            if len(self.edges) != 3:
                raise ValueError("Un triángulo debe tener tres lados!")

            a = self.edges[0].length
            b = self.edges[1].length
            c = self.edges[2].length

            return a == b == c # descubrí que se puede escribir así,
                               # no sabía, pensé que tenía que ser con "and".