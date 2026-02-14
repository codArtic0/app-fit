from fastapi import APIRouter, HTTPException
from backend.controllers.usuario_controller import cadastrar_usuario

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


@router.post("/")
def criar_usuario(pessoa: dict):
    try:
        dados = cadastrar_usuario(pessoa)
        return {
            "message": "Usuário cadastrado com sucesso",
            "dados": dados
        }

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro interno")
