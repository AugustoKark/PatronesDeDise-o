from abc import ABC, abstractmethod
from triangulofactorymethod import TrianguloFactoryMethod

if __name__ == '__main__':
    metodo = TrianguloFactoryMethod()
    triangulo = metodo.create_triangulo(10, 10, 10)
    print(triangulo.get_descripcion())
