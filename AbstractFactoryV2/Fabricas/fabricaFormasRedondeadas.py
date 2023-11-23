from Fabricas.fabricaAbstracta import FabricaAbstracta
from Fabricas.Formas.rectangulo_redondeado import RectanguloRedondeado
from Fabricas.Formas.cuadrado_redondeado import CuadradoRedondeado

class FabricaFormasRedondeadas(FabricaAbstracta):
    def getForma(self, tipoForma):
        if tipoForma is None:
            return None
        if tipoForma.upper() == "RECTANGULO":
            print("Dentro de FabricaFormasRedondeadas: se ha seleccionado un Rectangulo")
            return RectanguloRedondeado()
        elif tipoForma.upper() == "CUADRADO":
            print("Dentro de FabricaFormasRedondeadas: se ha seleccionado un Cuadrado")
            return CuadradoRedondeado()
        return None
    