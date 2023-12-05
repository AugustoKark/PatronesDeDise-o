from BaseHandler import BaseHandler

class Fireman(BaseHandler):
    def handle(self, request):
        if request == "Fireman":
            return "Fireman: I'll take care of it!"
        else:
            return super().handle(request)