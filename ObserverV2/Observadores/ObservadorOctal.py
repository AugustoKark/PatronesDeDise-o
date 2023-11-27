# observadores/ObservadorOctal.py
from Observadores.Observador import Observador

class ObservadorOctal(Observador):
    def __init__(self, sujeto):
        self.sujeto = sujeto
        self.sujeto.adjuntar(self)

    def actualizar(self):
        print("Cadena octal: " + oct(self.sujeto.obtener_estado())[2:])
