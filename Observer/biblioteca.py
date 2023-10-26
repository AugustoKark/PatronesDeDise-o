from alarma_libro import AlarmaLibro
class Biblioteca:
    def devuelve_libro(self, libro):
        if libro.estado == "MALO":
            alarma = AlarmaLibro()
            alarma.notify_observers()
