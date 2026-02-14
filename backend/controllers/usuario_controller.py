from backend.models.Usuario import Usuario

from sqlmodel import Session, select

def get_usuarios_db(session: Session):
    statement = select(Usuario)
    return session.exec(statement).all()

def get_usuario_por_id(id_usuario: int, session: Session):
    return session.get(Usuario, id_usuario)