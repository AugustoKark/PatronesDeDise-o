from handler import Handler

class ConcreteHandler2(Handler):
    def handle(self, request):
        if request.type == "tipo2":
            print("Manejador 2 ha manejado la solicitud")
            return True
        else:
            return False
