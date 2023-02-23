from entities.request import Request


class Handler:
    def set_next(self, handler: 'Handler'):
        pass
    
    def handle(self, request: Request) -> bool:
        pass