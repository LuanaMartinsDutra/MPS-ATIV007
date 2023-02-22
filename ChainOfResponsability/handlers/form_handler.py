from entities.request import Request

from handlers.basehandler import BaseHandler


class FormHandler(BaseHandler):
    def __init__(self):
        super().__init__()

    def handle(self, request: Request):
        if request.email == '' or request.password == '' or request.username == '':
            return False
        return super().handle(request)