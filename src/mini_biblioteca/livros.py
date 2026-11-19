import uuid

class Livro:

    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True
        self.codigo = str(uuid.uuid4())

