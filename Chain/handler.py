class Handler:
    def handle(self, request):
        pass

    def set_next(self, handler):
        self.next_handler = handler
