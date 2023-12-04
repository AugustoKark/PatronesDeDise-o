from Fabricas.Formas.forma import Forma

class Cuadrado(Forma):
    def dibujar(self):
        print("Dentro de Cuadrado::dibujar() método.")

    def imprimir(self):
            print("******")
            print("*    *")
            print("*    *")
            print("******")
            print("\n")