from abc import ABC, abstractmethod
from Productos.Empaque.botella import Botella
from Interfaces.item import Item


class BebidaFria(Item, ABC):
    def empaque(self):
        return Botella()

    @abstractmethod
    def precio(self):
        pass