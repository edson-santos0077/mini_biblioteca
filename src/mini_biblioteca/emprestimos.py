from .livros import Livro
from .usuarios import Usuario

class Emprestimo:

    def __init__(self, livro: Livro, usuario: Usuario):
        if not livro.disponivel:
            raise ValueError("O livro não está disponível")

        self.livro = livro
        self.usuario = usuario
        self.ativo = True

        self.livro.disponivel = False


    def devolver(self):
        self.ativo = False
        self.livro.disponivel = True

