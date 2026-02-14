from models.Usuario import Usuario

def cadastrar_usuario(pessoa: dict):
    try:
        nova_pessoa = Usuario(
            nome=pessoa["nome"],
            sexo=pessoa["sexo"],
            idade=pessoa["idade"],
            peso=pessoa["peso"],
            altura=pessoa["altura"],
            imc=pessoa["imc"],
            tmb=pessoa["tmb"]
        )

        return nova_pessoa.to_dict()

    except KeyError as e:
        raise ValueError(f"Campo obrigatório ausente: {e}")
