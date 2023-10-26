from subject import Subject
class AlarmaLibro(Subject):
    def __init__(self):
        self.observadores = []

    def attach(self, observer):
        self.observadores.append(observer)

    def dettach(self, observer):
        self.observadores.remove(observer)

    def notify_observers(self):
        for observador in self.observadores:
            observador.update()
