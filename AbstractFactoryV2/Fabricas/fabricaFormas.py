from Fabricas.fabricaAbstracta import FabricaAbstracta
from Fabricas.Formas.rectangulo import Rectangulo
from Fabricas.Formas.cuadrado import Cuadrado

class FabricaFormas(FabricaAbstracta):
    def getForma(self, tipoForma):
        if tipoForma is None:
            return None
        if tipoForma.upper() == "RECTANGULO":
            print("Dentro de FabricaFormas: se ha seleccionado un Rectangulo")
            return Rectangulo()
        elif tipoForma.upper() == "CUADRADO":
            print("Dentro de FabricaFormas: se ha seleccionado un Cuadrado")
            return Cuadrado()
        return None
    