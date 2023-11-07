from handler import Handler

class ConcreteHandler1(Handler):
    def handle(self, request):
        if request.type == "tipo1":
            print("Manejador 1 ha manejado la solicitud")
            return True
        else:
            return False
