from abc import ABC, abstractmethod
from Interfaces.empaque import Empaque
class Envoltura(Empaque):
    def empacar(self):
        return "Envoltura"
