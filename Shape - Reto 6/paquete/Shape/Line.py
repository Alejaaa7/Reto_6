# Line.py

from .Point import Point

class Line:
    def __init__(self, start_point: Point, end_point: Point):

        #Verificar que los puntos inicial y final sean Puntos:
        if not isinstance(start_point, Point) or not isinstance(end_point, Point):
            raise TypeError("Los valores ingresados para punto inicial y final\
deben ser puntos.")
        self.start_point = start_point
        self.end_point = end_point

        # Verificar que los puntos ingresados sean válidos
        if start_point.x == end_point.x and start_point.y == end_point.y:
            raise ValueError("Los puntos inicial y final no pueden ser el mismo.")

        self.length = start_point.compute_distance(end_point)


    