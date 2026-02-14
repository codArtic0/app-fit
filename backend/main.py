from models.Pessoa import Pessoa

nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo (masculino/feminino): ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))
nivel = input("Digite seu nível de atividade física (0-4): ")

pessoa = Pessoa(nome, sexo, idade, peso, altura, nivel)

print(f"Olá {pessoa.nome}, seu IMC é: {pessoa.imc:.2f} e sua TMB é: {pessoa.tmb:.2f} calorias por dia.")

print("Com base na sua TMB, suas necessidades calóricas diárias são:")
print(f"Proteínas: {pessoa.macros[0]:.2f} g")
print(f"Gorduras: {pessoa.macros[1]:.2f} g")
print(f"Carboidratos: {pessoa.macros[2]:.2f} g")