from abc import ABC, abstractmethod
from triangulo.triangulo import Triangulo

class Escaleno(Triangulo):

    def __init__(self, ladoA, ladoB, ladoC):
        super().__init__(ladoA, ladoB, ladoC)

    def get_descripcion(self):
        return "Es un triangulo Escaleno"

    def get_superficie(self, base, altura):
        return 0

    def dibujate(self):
        pass