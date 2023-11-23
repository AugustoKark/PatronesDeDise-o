from abc import ABC, abstractmethod

class FabricaAbstracta(ABC):
    @abstractmethod
    def getForma(self, tipoForma):
        pass