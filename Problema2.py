def obtener_calificaciones():
    while True:
        try:
            calificaciones = input("Ingrese las calificaciones separadas por comas (pueden ser decimales): ")

            lista_calificaciones = calificaciones.split(",")

            lista_calificaciones_redondeadas = [round(float(c.strip())) for c in lista_calificaciones]

            return lista_calificaciones_redondeadas
        
        except ValueError:
            print("Error: Por favor, asegúrese de ingresar solo números válidos (enteros o decimales) separados por comas.")

if __name__ == "__main__":
    calificaciones = obtener_calificaciones()
    print("Calificaciones ingresadas (redondeadas):", calificaciones)
