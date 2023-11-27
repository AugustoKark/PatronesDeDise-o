from abc import ABC, abstractmethod
from item import Item
from envoltura import Envoltura

class Hamburguesa(Item, ABC):
    def empaque(self):
        return Envoltura()

    @abstractmethod
    def precio(self):
        pass