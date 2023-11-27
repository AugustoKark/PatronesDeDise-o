from abc import ABC, abstractmethod

class Item(ABC):
    @abstractmethod
    def nombre(self):
        pass

    @abstractmethod
    def empaque(self):
        pass

    @abstractmethod
    def precio(self):
        pass