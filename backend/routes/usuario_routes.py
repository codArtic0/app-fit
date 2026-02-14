from fastapi import APIRouter, HTTPException
from backend.controllers.Usuario import cadastrar_usuario
from backend.models import Usuario

router = APIRouter()

@router.post("/cadastro")
async def cadastro(usuario: Usuario):
	return await cadastrar_usuario(usuario)

