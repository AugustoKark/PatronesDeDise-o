from Inventario import Inventario
from ComprarInventario import ComprarInventario
from VenderInventario import VenderInventario
from Brocker import Corredor

if __name__ == "__main__":
    inventario_abc = Inventario()

    orden_comprar = ComprarInventario(inventario_abc)
    orden_vender = VenderInventario(inventario_abc)

    corredor = Corredor()
    corredor.tomar_orden(orden_comprar)
    corredor.tomar_orden(orden_vender)

    corredor.realizar_ordenes()
