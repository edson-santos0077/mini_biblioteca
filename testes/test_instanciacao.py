from mini_biblioteca import Livro, Usuario, Emprestimo

def test_instanciacao_livro():
    livro = Livro("Dom Casmurro", "Machado de Assis")
    assert livro.titulo == "Dom Casmurro"
    assert livro.autor == "Machado de Assis"
    assert livro.disponivel is True
    assert livro.codigo is not None

def test_instanciacao_usuario():
    usuario = Usuario("Maria", "u100")
    assert usuario.nome == "Maria"
    assert usuario.idusuario == "u100"

def test_instanciacao_emprestimo():
    livro = Livro("1984", "George Orwell")
    usuario = Usuario("João", "u200")
    emprestimo = Emprestimo(livro, usuario)

    assert emprestimo.livro == livro
    assert emprestimo.usuario == usuario
    assert emprestimo.ativo is True
