from Fabricas.fabricaAbstracta import FabricaAbstracta
from Fabricas.Formas.rectangulo import Rectangulo
from Fabricas.Formas.cuadrado import Cuadrado

class FabricaFormas(FabricaAbstracta):
    def getForma(self, tipoForma):
        if tipoForma is None:
            return None
        if tipoForma.upper() == "RECTANGULO":
            return Rectangulo()
        elif tipoForma.upper() == "CUADRADO":
            return Cuadrado()
        return None
    