from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def dibujar(self):
        pass