import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def cuadrante(self):
        if self.x == 0 and self.y == 0:
            return "El punto está en el origen"
        elif self.x == 0:
            return "El punto está sobre el eje Y"
        elif self.y == 0:
            return "El punto está sobre el eje X"
        elif self.x > 0 and self.y > 0:
            return "El punto está en el primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return "El punto está en el segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return "El punto está en el tercer cuadrante"
        elif self.x > 0 and self.y < 0:
            return "El punto está en el cuarto cuadrante"

    def vector(self, otro_punto):
        return Punto(otro_punto.x - self.x, otro_punto.y - self.y)

    def distancia(self, otro_punto):
        return math.sqrt((otro_punto.x - self.x) ** 2 + (otro_punto.y - self.y) ** 2)


class Rectangulo:
    def __init__(self, punto1=Punto(), punto2=Punto()):
        self.punto1 = punto1
        self.punto2 = punto2

    def base(self):
        return abs(self.punto2.x - self.punto1.x)

    def altura(self):
        return abs(self.punto2.y - self.punto1.y)

    def area(self):
        return self.base() * self.altura()


if __name__ == "__main__":
    A = Punto(2, 3)
    B = Punto(5, 5)
    C = Punto(-3, -1)
    D = Punto(0, 0)

    print(A)
    print(B)
    print(C)
    print(D)

    print(A.cuadrante())
    print(C.cuadrante())
    print(D.cuadrante())

    print("Vector AB:", A.vector(B))
    print("Vector BA:", B.vector(A))

    print("Distancia A-B:", A.distancia(B))
    print("Distancia B-A:", B.distancia(A))

    rectangulo = Rectangulo(A, B)
    print("Base del rectángulo:", rectangulo.base())
    print("Altura del rectángulo:", rectangulo.altura())
    print("Área del rectángulo:", rectangulo.area())
