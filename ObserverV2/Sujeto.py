# sujeto/Sujeto.py

class Sujeto:
    def __init__(self):
        self.observadores = []
        self.estado = 0

    def adjuntar(self, observador):
        self.observadores.append(observador)

    def notificar_observadores(self):
        for observador in self.observadores:
            observador.actualizar()

    def establecer_estado(self, estado):
        self.estado = estado
        self.notificar_observadores()

    def obtener_estado(self):
        return self.estado
