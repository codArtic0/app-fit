from fastapi import APIRouter, HTTPException
from models import Pessoa

router = APIRouter()

@router.post("/cadastro")
def cadastrar_usuario(pessoa: dict):
    try:
        nova_pessoa = Pessoa(
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