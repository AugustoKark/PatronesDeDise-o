from AbstractLogger import AbstractLogger

class FileLogger(AbstractLogger):

    def __init__(self, nivel):
        super().__init__()
        self.level = nivel

    def escribir(self, mensaje):
        print(f"Archivo:Registrador: {mensaje}")
