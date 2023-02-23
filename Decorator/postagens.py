class Postagem():

    def criar_postagem(self):
        pass


class ConcretePostagem(Postagem):

    _post = "Criar uma postagem no...\n"

    def criar_postagem(self):
        return self._post


class PostagemDecorator(Postagem):

    def __init__(self, decorated_post):
        self.decorated_post = decorated_post


    def criar_postagem(self):
        return self.decorated_post.criar_postagem()


class Instagram(PostagemDecorator):

    _plataforma = "Instagram"

    def __init__(self, decorated_post):
        super().__init__(decorated_post)


    def criar_postagem(self):
        return f"{self.decorated_post.criar_postagem()} e {self._plataforma}"


class Linkedin(PostagemDecorator):

    _plataforma = "Linkedin"

    def __init__(self, decorated_post):
        super().__init__(decorated_post)

    def criar_postagem(self):
        return f"{self.decorated_post.criar_postagem()}  {self._plataforma}"


def mostrar_post():
    post = ConcretePostagem()
    post = Instagram((Linkedin(post)))
    print("Iniciando as postagens!")
    print(post.criar_postagem())
    print("-----Viagem para o México----- \n")

def profissional():
    post = ConcretePostagem()
    post = Linkedin(post)
    print("Manter perfil profissional")
    print(post.criar_postagem())
    print("-----Viagem a negócios para China----- \n")

if __name__ == '__main__':
    mostrar_post() 
    profissional()