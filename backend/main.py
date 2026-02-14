from models.Pessoa import Pessoa

nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo (masculino/feminino): ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

pessoa = Pessoa(nome, sexo, idade, peso, altura)
imc = pessoa.calcular_imc()
tmb = pessoa.calcular_tmb()

print(f"Olá {pessoa.nome}, seu IMC é: {imc:.2f} e sua TMB é: {tmb:.2f} calorias por dia.")