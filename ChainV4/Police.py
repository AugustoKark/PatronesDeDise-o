from BaseHandler import BaseHandler

class Police(BaseHandler):
    def handle(self, request):
        if request == "Police":
            return "Police: I'll take care of it!"
        else:
            return super().handle(request)