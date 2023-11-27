class Corredor:

    def __init__(self):
        self.lista_ordenes = []

    def tomar_orden(self, orden):
        self.lista_ordenes.append(orden)

    def realizar_ordenes(self):
        for orden in self.lista_ordenes:
            orden.ejecutar()
        self.lista_ordenes.clear()
