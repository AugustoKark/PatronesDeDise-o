from Orden import Orden

class VenderInventario(Orden):

    def __init__(self, inventario):
        self.inventario = inventario

    def ejecutar(self):
        self.inventario.vender()
