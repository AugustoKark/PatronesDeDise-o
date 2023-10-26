import abc
from alarma_libro import AlarmaLibro
from biblioteca import Biblioteca
from alarma_libro import AlarmaLibro
from biblioteca import Biblioteca
from compras import Compras
from stock import Stock
from libro import Libro

from administracion import Administracion

if __name__ == '__main__':
    print("Creando alarma y adjuntando observadores...")
    alarma = AlarmaLibro()
    alarma.attach(Compras())
    alarma.attach(Administracion())
    alarma.attach(Stock())

    libro = Libro("Libro de ejemplo", "MALO")
    print(f"Estado del libro: {libro.estado}")
    
    biblioteca = Biblioteca()
    print("Devolviendo libro a la biblioteca...")
    biblioteca.devuelve_libro(libro)
    print("Proceso de devolución del libro completado.")
