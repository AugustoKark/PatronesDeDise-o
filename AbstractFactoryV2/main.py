from Fabricas.productor import Productor

if __name__ == '__main__':
    fabrica = Productor.getFabrica(True)
    forma1 = fabrica.getForma("RECTANGULO")
    forma1.dibujar()
    forma2 = fabrica.getForma("CUADRADO")
    forma2.dibujar()
    fabrica = Productor.getFabrica(False)
    forma1 = fabrica.getForma("RECTANGULO")
    forma1.dibujar()
    forma2 = fabrica.getForma("CUADRADO")
    forma2.dibujar()