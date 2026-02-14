from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import List
from backend.database.db import get_session
from backend.controllers import usuario_controller
from backend.models.Usuario import Usuario

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.get("/", response_model=List[Usuario])
def listar_usuarios(session: Session = Depends(get_session)):
    usuarios = usuario_controller.get_usuarios_db(session)
    return usuarios

@router.get("/{usuario_id}", response_model=Usuario)
def detalhar_usuario(usuario_id: int, session: Session = Depends(get_session)):
    usuario = usuario_controller.get_usuario_por_id(usuario_id, session)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario