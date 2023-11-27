from abc import ABC, abstractmethod

class AbstractLogger(ABC):
    INFO = 1
    DEBUG = 2
    ERROR = 3

    def __init__(self):
        self.level = 0
        self.next_logger = None

    def set_siguiente_logger(self, siguiente_logger):
        self.next_logger = siguiente_logger

    def registrar_mensaje(self, nivel, mensaje):
        if self.level <= nivel:
            self.escribir(mensaje)
        if self.next_logger is not None:
            self.next_logger.registrar_mensaje(nivel, mensaje)

    @abstractmethod
    def escribir(self, mensaje):
        pass
