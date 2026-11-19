class Usuario:
    ids = set()
    def __init__(self, nome: str, idusuario: str):
        if idusuario in Usuario.ids:
            raise ValueError("O id dos usuários deve ser unico")

        self.nome = nome
        self.idusuario = idusuario

        Usuario.ids.add(idusuario)

