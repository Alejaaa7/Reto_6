# main.py

import paquete.Shape.Point as punto
import paquete.Shape.Line as linea
import paquete.Shape.Shape as forma

import paquete.Triangles.Triangles as triangulo
import paquete.Triangles.Equilateral as equi
import paquete.Triangles.Isosceles as iso
import paquete.Triangles.Scalene as sca
import paquete.Triangles.TriRectangle as rec


import paquete.Rectangle.Rectangle as rectangulo
import paquete.Rectangle.Square as cuadrado

def main():
    print("1. Probando clases base: ")
    x1 = 0
    y1 = 0
    x2 = 3
    y2 = 4

    print(" - Con punto inicial (0, 0) y final (3, 4):")
    punto_inicial = punto.Point(x1, y1)
    punto_final = punto.Point(x2, y2)
    print("    La distancia entre los puntos es = ", \
          punto_inicial.compute_distance(punto_final))

    print(" - Línea generada con esos puntos:")
    linea1 = linea.Line(punto_inicial, punto_final)
    print("    El largo de la línea es = ", linea1.length)


    print("2. Probando Triangles:")
    print(" - Para probar un tríangulo general:")
    pt1 = punto.Point(0, 0)
    pt2 = punto.Point(4, 0)
    pt3 = punto.Point(0, 3)
    tri1 = triangulo.Triangles(pt1, pt2, pt3)
    print("    Perímetro = ", tri1.compute_perimeter())
    print("    Área = ", tri1.compute_area())
    print("    Ángulos = ", tri1.compute_inner_angles())   

    print(" - Probando Isosceles: ")
    pis1 = punto.Point(0, 0)
    pis2 = punto.Point(2, 3)
    pis3 = punto.Point(4, 0)
    iso1 = iso.Isosceles(pis1, pis2, pis3)
    print("    Perímetro Isosceles = ", iso1.compute_perimeter())
    print("    Área Isosceles = ", iso1.compute_area())
    print("    Ángulos Isosceles = ", iso1.compute_inner_angles())

    print(" - Probando Equilateral: ")
    peq1 = punto.Point(0, 0)
    peq2 = punto.Point(1, 3 ** 0.5)
    peq3 = punto.Point(2, 0)
    equi1 = equi.Triangles(peq1, peq2, peq3)
    print("    Perímetro equilatero = ", equi1.compute_perimeter())
    print("    Área equilatero = ", equi1.compute_area())
    print("    Ángulos equilatero = ", equi1.compute_inner_angles())

    print(" - Probando Scalene: ")
    pes1 = punto.Point(0, 0)
    pes2 = punto.Point(3, 0)
    pes3 = punto.Point(2, 2)
    sca1 = sca.Triangles(pes1, pes2, pes3)
    print("    Perímetro escaleno = ", sca1.compute_perimeter())
    print("    Área escaleno = ", sca1.compute_area())
    print("    Ángulos escaleno = ", sca1.compute_inner_angles())

    print(" - Probando TriRectangle: ")
    ptr1 = punto.Point(0, 0)
    ptr2 = punto.Point(0, 4)
    ptr3= punto.Point(3, 0)
    trirec1 = rec.Triangles(ptr1, ptr2, ptr3)
    print("    Perímetro triángulo rectángulo = ", trirec1.compute_perimeter())
    print("    Área triángulo rectángulo = ", trirec1.compute_area())
    print("    Ángulos triángulo rectángulo = ", trirec1.compute_inner_angles())


    print("3. Probando Rectangle:")
    pre1 = punto.Point(0, 0)
    pre2 = punto.Point(0, 2)
    pre3 = punto.Point(4, 0)
    pre4 = punto.Point(4, 2)
    rectangle1 = rectangulo.Rectangle(pre1, pre2, pre3, pre4)
    print("    Perímetro rectángulo = ", rectangle1.compute_perimeter())
    print("    Área rectángulo = ", rectangle1.compute_area())
    print("    Ángulos rectángulo = ", rectangle1.compute_inner_angles())

    print(" - Probando Square: ")
    pcu1 = punto.Point(0, 0)
    pcu2 = punto.Point(0, 2)
    pcu3 = punto.Point(2, 0)
    pcu4 = punto.Point(2, 2)
    square1 = cuadrado.Square(pcu1, pcu2, pcu3, pcu4)
    print("    Perímetro cuadrado = ", square1.compute_perimeter())
    print("    Área cuadrado = ", square1.compute_area())
    print("    Ángulos cuadrado = ", square1.compute_inner_angles())

    print("Fin de la prueba. Gracias :).")

if __name__ == "__main__":
    main()