from Orden import Orden

class ComprarInventario(Orden):
    
    def __init__(self, inventario):
        self.inventario = inventario

    def ejecutar(self):
        self.inventario.comprar()
