import pytest
from mini_biblioteca import Livro, Usuario, Emprestimo

def test_emprestimo_torna_livro_indisponivel():
    livro = Livro("O Hobbit", "Tolkien")
    usuario = Usuario("Carlos", "u300")

    Emprestimo(livro, usuario)
    assert livro.disponivel is False

def test_nao_pode_emprestar_livro_indisponivel():
    livro = Livro("Duna", "Frank Herbert")
    u1 = Usuario("Ana", "u400")
    u2 = Usuario("Pedro", "u401")

    Emprestimo(livro, u1)

    with pytest.raises(ValueError):
        Emprestimo(livro, u2)

def test_devolucao_libera_livro_e_encerra_emprestimo():
    livro = Livro("Fundação", "Isaac Asimov")
    usuario = Usuario("Julia", "u500")

    emprestimo = Emprestimo(livro, usuario)
    emprestimo.devolver()

    assert emprestimo.ativo is False
    assert livro.disponivel is True

def test_usuario_id_unico():
    Usuario("Lucas", "u600")
    with pytest.raises(ValueError):
        Usuario("Marcos", "u600")
