class Comida:
    def __init__(self):
        self.items = []

    def agregar_item(self, item):
        self.items.append(item)

    def obtener_costo(self):
        costo = 0.0
        for item in self.items:
            costo += item.precio()
        return costo

    def mostrar_items(self):
        for item in self.items:
            print("Item: " + item.nombre() + ", Empaque: " + item.empaque().empacar() + ", Precio: " + str(item.precio()))

