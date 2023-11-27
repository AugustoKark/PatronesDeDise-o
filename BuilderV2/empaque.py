from abc import ABC, abstractmethod
class Empaque(ABC):
    @abstractmethod
    def empacar(self):
        pass