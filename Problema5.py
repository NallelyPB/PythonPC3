class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = []

    def display(self):
        print(f"Nombre: {self.nombre}")
        print(f"Número de registro: {self.numero_registro}")
        if self.edad is not None:
            print(f"Edad: {self.edad}")
        else:
            print("Edad: No asignada")
        
        if self.notas:
            print(f"Notas: {', '.join(map(str, self.notas))}")
        else:
            print("Notas: No asignadas")

    def setAge(self, edad):
        self.edad = edad

    def setNota(self, *notas):
        self.notas.extend(notas)

if __name__ == "__main__":
    alumno1 = Alumno("Sara Cobos", 101)
    alumno1.display()
    alumno1.setAge(20)
    alumno1.setNota(95, 87, 92)
    print("\nInformación actualizada del estudiante:")
    alumno1.display()
