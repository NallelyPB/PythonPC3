class Producto:
    def __init__(self, nombre, tipo, año, precio):
        self.nombre = nombre
        self.tipo = tipo
        self.año = año
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - Tipo: {self.tipo}, Año: {self.año}, Precio: ${self.precio:.2f}"


class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos en el catálogo.")
            return
        print("Catálogo de productos:")
        for producto in self.productos:
            print(producto)

    def filtrar_por_año(self, año):
        productos_filtrados = [p for p in self.productos if p.año == año]
        return productos_filtrados

    def filtrar_por_tipo(self, tipo):
        productos_filtrados = [p for p in self.productos if p.tipo.lower() == tipo.lower()]
        return productos_filtrados


if __name__ == "__main__":
    catalogo = Catalogo()

    producto1 = Producto("Batería", "Eléctrico", 2020, 120.50)
    producto2 = Producto("Frenos", "Frenos", 2019, 85.75)
    producto3 = Producto("Amortiguador", "Suspensión", 2021, 150.00)

    catalogo.agregar_producto(producto1)
    catalogo.agregar_producto(producto2)
    catalogo.agregar_producto(producto3)

    catalogo.mostrar_productos()

    print("\nFiltrando productos por año 2020:")
    productos_2020 = catalogo.filtrar_por_año(2020)
    for producto in productos_2020:
        print(producto)

    print("\nFiltrando productos por tipo 'Frenos':")
    productos_frenos = catalogo.filtrar_por_tipo("Frenos")
    for producto in productos_frenos:
        print(producto)
