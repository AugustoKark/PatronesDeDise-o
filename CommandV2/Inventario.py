class Inventario:

    def __init__(self):
        self.nombre = "ABC"
        self.cantidad = 10

    def comprar(self):
        print(f"Inventario [ Nombre: {self.nombre}, Cantidad: {self.cantidad} ] comprado")

    def vender(self):
        print(f"Inventario [ Nombre: {self.nombre}, Cantidad: {self.cantidad} ] vendido")
