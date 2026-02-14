from models.Usuario import Usuario
from fastapi import HTTPException


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
        return {"message": "Usuário cadastrado com sucesso!", "dados": nova_pessoa.to_dict()}
    except KeyError as e:
        raise HTTPException(status_code=400, detail=f"Campo obrigatório ausente: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))