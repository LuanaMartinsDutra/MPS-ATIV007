from handler import Handler
from request import Request


class BaseHandler(Handler):

    def __init__(self):
        super().__init__()
        self.next: Handler = None

    def set_next(self, handler: 'Handler'):
        self.next = handler

    def handle(self, request: Request):
        print(request)
