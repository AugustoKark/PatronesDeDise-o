from BaseHandler import BaseHandler

class Medic(BaseHandler):
    def handle(self, request):
        if request == "Medic":
            return "Medic: I'll take care of it!"
        else:
            return super().handle(request)