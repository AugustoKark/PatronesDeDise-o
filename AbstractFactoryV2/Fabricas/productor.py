
from .fabricaFormas import FabricaFormas
from .fabricaFormasRedondeadas import FabricaFormasRedondeadas

class Productor:
    @staticmethod
    def getFabrica(tipoFabrica):
      
        if tipoFabrica:
            print("Fabrica de formas comunes seleccionada")
            return FabricaFormas()
        else:
            print("Fabrica de formas redondeadas seleccionada")
            return FabricaFormasRedondeadas()
        