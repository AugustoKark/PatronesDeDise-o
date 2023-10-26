# ilibro_mal_estado.py
from abc import ABC, abstractmethod

class ILibroMalEstado(ABC):
    @abstractmethod
    def update(self):
        pass
