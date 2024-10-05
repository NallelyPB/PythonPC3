def obtener_fraccion():
    while True:
        try:
            fraccion = input("Ingrese la fracción en formato X/Y: ")
            
            x_str, y_str = fraccion.split("/")
            
            x = int(x_str)
            y = int(y_str)

            if y == 0:
                raise ZeroDivisionError("El denominador no puede ser cero.")
            if x > y:
                raise ValueError("El numerador no puede ser mayor que el denominador.")

            porcentaje = (x / y) * 100

            if porcentaje <= 1:
                return "E"
            elif porcentaje >= 99:
                return "F"
            else:
                return f"{round(porcentaje)}%"
        
        except ValueError:
            print("Error: Ingrese dos números enteros separados por una barra (/). Asegúrese de que X ≤ Y.")
        except ZeroDivisionError:
            print("Error: El denominador no puede ser cero.")

if __name__ == "__main__":
    resultado = obtener_fraccion()
    print("Resultado:", resultado)
