# from comida import Comida
# from hamburguesa_vegetariana import HamburguesaVegetariana
# from hamburguesa_pollo import HamburguesaPollo
# from coca_cola import CocaCola
# from pepsi import Pepsi
from Comida.comida import Comida
from Productos.Hamburgesa.hamburguesa_vegetariana import HamburguesaVegetariana
from Productos.Hamburgesa.hamburguesa_pollo import HamburguesaPollo
from Productos.BebidasFrias.coca_cola import CocaCola
from Productos.BebidasFrias.pepsi import Pepsi

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