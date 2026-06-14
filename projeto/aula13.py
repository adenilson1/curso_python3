print("### PROGRAMA QUE CALCULA O IMC DE UMA PESSOA ###\n")

# Dados da pessoa
nome = input("Digite o seu nome: ")
altura_em_metros = float(input("\nDigite o seu peso em metros: "))
peso_quilos = int(input("\nDigite o seu peso em Kilogramas: "))

# Cálculo do IMC
imc = peso_quilos/(altura_em_metros ** 2)

# Imprimi o valor do IMC
linha_1 = f'\n{nome} tem {altura_em_metros:.2f} de altura,'
linha_2 = f'pesa {peso_quilos} quilos e IMC é {imc:.2f}'
print(linha_1)
print(linha_2)