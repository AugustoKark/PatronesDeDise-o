from abc import ABC, abstractmethod
from item import Item
from botella import Botella


class BebidaFria(Item, ABC):
    def empaque(self):
        return Botella()

    @abstractmethod
    def precio(self):
        pass