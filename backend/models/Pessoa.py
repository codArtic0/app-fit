class Pessoa:
    def __init__(self, nome, sexo, idade, peso, altura, total_calorias=0, agua=0, sono=0, exercicio=0, imc=0, tmb=0):
        self.nome = nome
        self.sexo = sexo
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.imc = imc
        self.tmb = tmb

    def calcular_imc(self):
        self.imc = self.peso / (self.altura ** 2)
        return self.imc
    def calcular_tmb(self):
        if self.sexo == 'masculino':
            self.tmb = 88.36 + (13.4 * self.peso) + (4.8 * self.altura * 100) - (5.7 * self.idade)
        else:
            self.tmb = 447.6 + (9.2 * self.peso) + (3.1 * self.altura * 100) - (4.3 * self.idade)
        return self.tmb