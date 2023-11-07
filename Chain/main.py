# from handler import Handler
from concrete_handler1 import ConcreteHandler1
from concrete_handler2 import ConcreteHandler2
from request import Request

def client_code(chain):
    request = Request("tipo1")
    print("Enviando solicitud...")
    chain.handle(request)


def main():
    chain = ConcreteHandler1()
    chain.set_next(ConcreteHandler2())

    # Usamos la cadena de responsabilidad
    client_code(chain)

if __name__ == "__main__":
    main()
