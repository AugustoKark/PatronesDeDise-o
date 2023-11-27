# from comida import Comida
# from hamburguesa_vegetariana import HamburguesaVegetariana
# from hamburguesa_pollo import HamburguesaPollo
# from coca_cola import CocaCola
# from pepsi import Pepsi
from Productos.comida import Comida
from Formas.Hamburgesa.hamburguesa_vegetariana import HamburguesaVegetariana
from Formas.Hamburgesa.hamburguesa_pollo import HamburguesaPollo
from Formas.BebidasFrias.coca_cola import CocaCola
from Formas.BebidasFrias.pepsi import Pepsi

class ConstructorComida:
    def preparar_comida_vegetariana(self):
        comida = Comida()
        comida.agregar_item(HamburguesaVegetariana())
        comida.agregar_item(CocaCola())
        return comida

    def preparar_comida_no_vegetariana(self):
        comida = Comida()
        comida.agregar_item(HamburguesaPollo())
        comida.agregar_item(Pepsi())
        return comida