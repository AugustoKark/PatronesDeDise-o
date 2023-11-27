from abc import ABC, abstractmethod
from Interfaces.item import Item
from Formas.Empaque.envoltura import Envoltura

class Hamburguesa(Item, ABC):
    def empaque(self):
        return Envoltura()

    @abstractmethod
    def precio(self):
        pass