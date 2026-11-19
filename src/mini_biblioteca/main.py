from mini_biblioteca import Emprestimo, Usuario, Livro

def main():
    usuario = Usuario("Edson", "1234")
    livro = Livro("O Auto da Compadecida", "Ariano Suassuna")
    emprestimo = Emprestimo(livro, usuario)
    print(f"Livro '{livro.titulo}' emprestado para {usuario.nome}. Disponível: {livro.disponivel}")
    emprestimo.devolver()
    print(f"Livro '{livro.titulo}' devolvido por {usuario.nome}. Disponível: {livro.disponivel}")

if __name__ == "__main__":
    main()
