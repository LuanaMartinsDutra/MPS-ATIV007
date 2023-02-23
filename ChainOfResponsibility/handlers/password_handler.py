from re import *

from entities.request import Request

from handlers.basehandler import BaseHandler


class PasswordHandler(BaseHandler):
    def __init__(self):
        super().__init__()

    def __find_pattern(self, pattern: str, value: str) -> bool:
        matches = findall(pattern, value)
        return len(matches) > 0

    def handle(self, request: Request):
        if not (
            self.__find_pattern('[0-9]+', request.password) and 
            self.__find_pattern('[a-zA-Z]+', request.password)
        ):
            return False
        return super().handle(request)