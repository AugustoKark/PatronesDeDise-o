from AbstractLogger import AbstractLogger

class ErrorLogger(AbstractLogger):

    def __init__(self, nivel):
        super().__init__()
        self.level = nivel

    def escribir(self, mensaje):
        print(f"Consola de Errores:Registrador: {mensaje}")
