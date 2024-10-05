import math

class CIRCULO:
    def __init__(self, radio):
        self.radio = radio
    def calcular_area(self):
        return math.pi * (self.radio ** 2)

if __name__ == "__main__":
    circulo1 = CIRCULO(3)
    circulo2 = CIRCULO(5)

    print(f"El área del círculo con radio {circulo1.radio} es: {circulo1.calcular_area():.2f}")
    print(f"El área del círculo con radio {circulo2.radio} es: {circulo2.calcular_area():.2f}")
