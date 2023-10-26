

from triangulo.escaleno import Escaleno
from triangulo.equilatero import Equilatero
from triangulo.isosceles import Isosceles


class TrianguloFactoryMethod:

    @staticmethod
    def create_triangulo(ladoA, ladoB, ladoC):
        if ladoA == ladoB == ladoC:
            return Equilatero(ladoA, ladoB, ladoC)
        elif ladoA != ladoB != ladoC != ladoA:
            return Escaleno(ladoA, ladoB, ladoC)
        else:
            return Isosceles(ladoA, ladoB, ladoC)