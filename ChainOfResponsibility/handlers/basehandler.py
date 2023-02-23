from entities.request import Request

from handlers.handler import Handler


class BaseHandler(Handler):

    def __init__(self):
        super().__init__()
        self.next: Handler = None

    def set_next(self, handler: 'Handler'):
        self.next = handler

    def handle(self, request: Request) -> bool:
        if self.next != None:
            return self.next.handle(request)
        return True
