from .hamburguesa import Hamburguesa

class HamburguesaVegetariana(Hamburguesa):
    def precio(self):
        return 25.0

    def nombre(self):
        return "Hamburguesa Vegetariana"