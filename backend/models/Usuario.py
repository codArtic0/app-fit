from sqlmodel import SQLModel, Field
from typing import Optional

from sqlmodel import SQLModel, Field
from typing import Optional

class UsuarioCreate(SQLModel):
    nome: str
    sexo: str
    altura: float
    idade: int
    peso: float
    nivel: int

class Usuario(UsuarioCreate, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    imc: float = 0.0
    tmb: float = 0.0


    def validar_dados(self):
        erros = {}
        if self.sexo not in ["m", "f"]:
            erros["sexo"] = "Sexo deve ser 'm' ou 'f'"
        if not (0 <= self.nivel <= 4):
            erros["nivel"] = "Nível deve ser entre 0 e 4"
        if self.peso <= 0:
            erros["peso"] = "Peso deve ser maior que zero"
        
        if erros:
            raise ValueError(erros)


    def calcular_imc(self):
        self.imc = round(self.peso / (self.altura ** 2), 2)

    def calcular_tmb(self):
        if self.sexo == 'masculino':
            self.tmb = 88.36 + (13.4 * self.peso) + (4.8 * self.altura * 100) - (5.7 * self.idade)
        else:
            self.tmb = 447.6 + (9.2 * self.peso) + (3.1 * self.altura * 100) - (4.3 * self.idade)

    def aplicar_nivel_atividade(self):
        fatores = {
            0: 1.2,
            1: 1.375,
            2: 1.55,
            3: 1.725,
            4: 1.9
        }
        self.tmb *= fatores[self.nivel]
        self.tmb = round(self.tmb, 2)

    def calcular_macros(self):
        proteinas = round(self.peso * 2.2, 2)
        gorduras = round(self.peso * 1.0, 2)
        carboidratos = round((self.tmb - (proteinas * 4) - (gorduras * 9)) / 4, 2)

        self.macros = {
            "proteinas": proteinas,
            "gorduras": gorduras,
            "carboidratos": carboidratos
        }

    def to_dict(self):
        return {
            "nome": self.nome,
            "sexo": self.sexo,
            "idade": self.idade,
            "peso": self.peso,
            "altura": self.altura,
            "nivel": self.nivel,
            "imc": self.imc,
            "tmb": self.tmb,
            "macros": self.macros
        }
