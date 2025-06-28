# Rectangle.py

from ..Shape.Point import Point
from ..Shape.Line import Line
from ..Shape.Shape import Shape

class Rectangle(Shape):
    def __init__(self, p1: Point, p2: Point, p3: Point, p4: Point):
        super().__init__()

        #Validar que los puntos dados sí sean puntos:
        if not isinstance(p1, Point) or not isinstance(p2, Point) \
            or not isinstance(p3, Point) or not isinstance(p4, Point):
            raise ValueError("Los vértices ingresados deben ser puntos.")
        
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        
        self.vertices = [p1, p2, p3, p4]
        self.edges = [Line(p1, p2),
                      Line(p2, p4),
                      Line(p4, p3),
                      Line(p3, p1)]
        
        a = self.edges[0].length
        b = self.edges[1].length
        c = self.edges[2].length
        d = self.edges[3].length
        # Validar que tiene dos lados opuestos:
        if not (a == c and b == d):
            raise ValueError("Los lados opuestos deben ser iguales.")


        self.inner_angles = self.compute_inner_angles()
        self.is_regular = self.check_if_is_regular()

    def compute_area(self):

        # Validar primero que sí tenga cuatro lados:
        if len(self.edges) != 4:
            raise ValueError("Esta figura debe tener CUATRO lados!")
            
        a = self.edges[0].length
        b = self.edges[1].length

        return a * b
       
    def compute_perimeter(self):

        if len(self.edges) != 4:
            raise ValueError("Esta figura debe tener CUATRO lados!")
        
        a = self.edges[0].length
        b = self.edges[1].length
        c = self.edges[2].length
        d = self.edges[3].length

        return a + b + c + d
      
    def compute_inner_angles(self):
        return [90, 90, 90, 90]
