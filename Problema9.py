from Problema3 import CIRCULO
from Problema4 import RECTANGULO
from Problema4 import CUADRADO


def validar_entrada(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("Error: El valor debe ser positivo.")
        except ValueError:
            print("Error: Debes ingresar un número válido.")

def mostrar_menu():
    print("\nMenú de Cálculo de Áreas:")
    print("1. Calcular el área de un círculo")
    print("2. Calcular el área de un rectángulo")
    print("3. Calcular el área de un cuadrado")
    print("4. Salir")

def ejecutar_opcion(opcion):
    if opcion == 1:
        radio = validar_entrada("Introduce el radio del círculo: ")
        circulo = CIRCULO(radio)
        print(f"El área del círculo es: {circulo.calcular_area():.2f}")
    elif opcion == 2:
        largo = validar_entrada("Introduce el largo del rectángulo: ")
        ancho = validar_entrada("Introduce el ancho del rectángulo: ")
        rectangulo = RECTANGULO(largo, ancho)
        print(f"El área del rectángulo es: {rectangulo.calcular_area():.2f}")
    elif opcion == 3:
        lado = validar_entrada("Introduce el lado del cuadrado: ")
        cuadrado = CUADRADO(lado)
        print(f"El área del cuadrado es: {cuadrado.calcular_area():.2f}")
    elif opcion == 4:
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Por favor, elige una opción entre 1 y 4")

def main():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Elige una opción: "))
            if opcion == 4:
                ejecutar_opcion(opcion)
                break
            else:
                ejecutar_opcion(opcion)
        except ValueError:
            print("Error: Debes ingresar un número válido.")

if __name__ == "__main__":
    main()
