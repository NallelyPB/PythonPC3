class RECTANGULO:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho

class CUADRADO(RECTANGULO):
    def __init__(self, lado):
        super().__init__(lado, lado)

if __name__ == "__main__":
    rectangulo = RECTANGULO(4, 6)
    cuadrado = CUADRADO(5)

    print(f"El área del rectángulo (4x6) es: {rectangulo.calcular_area()}")
    print(f"El área del cuadrado (5x5) es: {cuadrado.calcular_area()}")
