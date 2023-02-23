from re import match

from entities.request import Request

from handlers.basehandler import BaseHandler


class EmailHandler(BaseHandler):
    def __init__(self):
        super().__init__()

    def handle(self, request: Request) -> bool:
        if not match('^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*?@[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)+$', request.email):
            return False
        return super().handle(request)