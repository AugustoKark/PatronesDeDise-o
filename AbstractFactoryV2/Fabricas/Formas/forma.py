from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def dibujar(self):
        pass

    @abstractmethod
    def imprimir(self):
        pass