
from buildercomida import ConstructorComida
if __name__ == "__main__":
    constructor_comida = ConstructorComida()

    comida_vegetariana = constructor_comida.preparar_comida_vegetariana()
    print("Comida Vegetariana")
    comida_vegetariana.mostrar_items()
    print("Costo Total:", comida_vegetariana.obtener_costo())

    comida_no_vegetariana = constructor_comida.preparar_comida_no_vegetariana()
    print("\n\nComida No Vegetariana")
    comida_no_vegetariana.mostrar_items()
    print("Costo Total:", comida_no_vegetariana.obtener_costo())