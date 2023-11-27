# observadores/ObservadorBinario.py
from Observadores.Observador import Observador

class ObservadorBinario(Observador):
    def __init__(self, sujeto):
        self.sujeto = sujeto
        self.sujeto.adjuntar(self)

    def actualizar(self):
        print("Cadena binaria: " + bin(self.sujeto.obtener_estado())[2:])
