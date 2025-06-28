# Point.py

class Point:
    def __init__(self, x: int, y: int):
        # Validar que x y y sean números enteros:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("x y y deben ser números.")
        
        self.x = x
        self.y = y
    
    def compute_distance(self, point):
        # Validar que el argumento sea un punto (o sea una instancia de Point.)
        if not isinstance(point, Point):
            raise TypeError("El argumento debe ser un punto.")

        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
