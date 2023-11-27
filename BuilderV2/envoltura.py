from abc import ABC, abstractmethod
from empaque import Empaque
class Envoltura(Empaque):
    def empacar(self):
        return "Envoltura"
