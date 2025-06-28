# Shape.py

class Shape:
    def __init__(self):
        self.is_regular = None
        self.vertices = []
        self.edges = []
        self.inner_angles = []

    def compute_area(self):
        raise NotImplementedError("Todas las subclases deben contener \
 'compute_area()'.")
    
    def compute_perimeter(self):
        raise NotImplementedError("Todas las subclases deben contener \
 'compute_perimeter()'.")
    
    def compute_inner_angles(self):
        raise NotImplementedError("Todas las subclases deben contener \
 'compute_inner_angles()'.")
    
    def check_if_is_regular(self):

        # Verificar que edges e inner_angles sean listas:
        if not isinstance(self.edges, list) or not \
            isinstance(self.inner_angles, list):
            raise TypeError("Tanto los lados como los ángulos deben ser listas.")
        
        # Verificar que no estén vacías:
        if not self.edges or not self.inner_angles:
            return False
        
        if all(i == self.edges[0].length for i in self.edges) and \
        all(i == self.inner_angles[0] for i in self.inner_angles):
            return True
        
        else:
            return False