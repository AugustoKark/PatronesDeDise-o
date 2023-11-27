# observadores/ObservadorHexadecimal.py
from Observadores.Observador import Observador

class ObservadorHexadecimal(Observador):
    def __init__(self, sujeto):
        self.sujeto = sujeto
        self.sujeto.adjuntar(self)

    def actualizar(self):
        print("Cadena hexadecimal: " + hex(self.sujeto.obtener_estado())[2:].upper())
