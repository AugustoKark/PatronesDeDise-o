from abc import ABC, abstractmethod

class Orden(ABC):
    @abstractmethod
    def ejecutar(self):
        pass
