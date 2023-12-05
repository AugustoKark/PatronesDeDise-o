from Handler import Handler
from abc import ABC, abstractmethod

class BaseHandler(Handler):
    def __init__(self):
        self.next_handler = None

    
    def set_next(self, handler):
        self.next_handler = handler
        return handler
    
    @abstractmethod
    def handle(self, request):
        if self.next_handler:
            return self.next_handler.handle(request)
        return None