class Pessoa:
    def __init__(self, nome, sexo, idade, peso, altura,nivel):
        self.nome = nome
        self.sexo = sexo
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.nivel = nivel
        self.calcular_imc()
        self.calcular_tmb()
        self.calcular_nivel_atividade(nivel)
        self.calcular_macros()


    def calcular_imc(self):
        self.imc = self.peso / (self.altura ** 2)
    
    def calcular_tmb(self):
        if self.sexo == 'masculino':
            self.tmb = 88.36 + (13.4 * self.peso) + (4.8 * self.altura * 100) - (5.7 * self.idade)
        else:
            self.tmb = 447.6 + (9.2 * self.peso) + (3.1 * self.altura * 100) - (4.3 * self.idade)
    
    def calcular_macros(self):
            proteinas = self.peso * 2.2
            gorduras = self.peso * 1.0
            carboidratos = (self.tmb - (proteinas * 4) - (gorduras * 9)) / 4
            self.macros = (proteinas, gorduras, carboidratos)

    def calcular_nivel_atividade(self, nivel):
        if nivel == '0':
            self.tmb *= 1.2
        elif nivel == '1':
            self.tmb *= 1.375
        elif nivel == '2':
            self.tmb *= 1.55
        elif nivel == '3':
            self.tmb *= 1.725
        elif nivel == '4':
            self.tmb *= 1.9