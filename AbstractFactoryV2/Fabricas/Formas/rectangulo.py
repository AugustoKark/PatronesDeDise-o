from Fabricas.Formas.forma import Forma

class Rectangulo(Forma):
    def dibujar(self):
        print("Dentro de Rectangulo::dibujar() método.")

    #make a rectangle to print with *
    def imprimir(self):
        print("******************************")
        print("*                            *")
        print("*                            *")
        print("******************************")
        print("\n")