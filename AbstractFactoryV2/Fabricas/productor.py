
from .fabricaFormas import FabricaFormas
from .fabricaFormasRedondeadas import FabricaFormasRedondeadas

class Productor:
    @staticmethod
    def getFabrica(tipoFabrica):
      
        if tipoFabrica:
            return FabricaFormas()
        else:
            return FabricaFormasRedondeadas()
        