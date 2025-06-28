# Triangles

from ..Shape.Point import Point
from ..Shape.Line import Line
from ..Shape.Shape import Shape

from math import degrees, acos


# Voy a abreviar algunos nombres, para mayor facilidad
class Triangles(Shape):
    def __init__(self, p1: Point, p2: Point, p3: Point):
        super().__init__()

        # Validar que los p1, 2 y 3 sean puntos:
        if not isinstance(p1, Point) or not isinstance(p2, Point) \
            or not isinstance(p3, Point):
            raise TypeError("Los valores de los vértices deben ser puntos.")
        
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

        self.vertices = [p1, p2, p3]
        self.edges = [Line(p1, p2),
                      Line(p2, p3),
                      Line(p3, p1)]
        self.compute_inner_angles = self.compute_inner_angles
        self.is_regular = self.check_if_is_regular()

    def compute_inner_angles(self):
        try:
            a = self.edges[0].length
            b = self.edges[1].length
            c = self.edges[2].length
            angle_A = degrees(acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)))
            angle_B = degrees(acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c)))
            angle_C = degrees(acos((a ** 2 + b ** 2 - c ** 2 ) / (2 * a * b)))
            return [angle_A, angle_B, angle_C]
            
        except ZeroDivisionError:
            raise ZeroDivisionError("Ocurrió una división por cero al \
 calcular los ángulos, por favor revisa los lados.")
            
        except ValueError as error:
            raise ValueError(f"Error en el cálculo de los ángulos {error}.")
            
    def compute_area(self):

        # Validar que sea un triángulo:
        if len(self.edges) != 3:
            raise ValueError("Un triángulodebe tener tres lados.")
        a = self.edges[0].length
        b = self.edges[1].length
        c = self.edges[2].length

        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

        return area
       
    def compute_perimeter(self):
        return self.edges[0].length + self.edges[1].length + \
                self.edges[2].length