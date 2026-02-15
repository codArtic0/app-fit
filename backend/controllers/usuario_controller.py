from backend.models.Usuario import Usuario

from sqlmodel import Session, select

def calcular_imc(peso: float, altura: float) -> float:
    return round(peso / (altura ** 2), 2)

def calcular_tmb(peso: float, altura: float, idade: int, sexo: str) -> float:
    if sexo.lower() == "m":
        return round(66.47 + (13.75 * peso) + (5.003 * altura * 100) - (6.755 * idade), 2)
    else:
        return round(655.1 + (9.563 * peso) + (1.85 * altura * 100) - (4.676 * idade), 2)

def get_usuarios_db(session: Session):
    statement = select(Usuario)
    return session.exec(statement).all()

def get_usuario_por_id(id_usuario: int, session: Session):
    return session.get(Usuario, id_usuario)

def criar_usuario_db(usuario: Usuario, session: Session):
    usuario.validar_dados()
    usuario.imc = calcular_imc(usuario.peso, usuario.altura)
    usuario.tmb = calcular_tmb(usuario.peso, usuario.altura, usuario.idade,usuario.sexo)
    session.add(usuario)
    session.commit()
    session.refresh(usuario)
    return usuario