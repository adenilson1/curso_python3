print("### PROGRAMA QUE CALCULA O IMC DE UMA PESSOA ###\n")

# Dados da pessoa
nome = input("Digite o seu nome: ")
altura_em_metros = float(input("\nDigite o seu peso em metros: "))
peso_quilos = int(input("\nDigite o seu peso em Kilogramas: "))

# Cálculo do IMC
imc = peso_quilos/(altura_em_metros ** 2)

# Imprimi o valor do IMC
print(f"""\n{nome} tem {altura_em_metros:.2f} de altura,
peso {peso_quilos} quilos e seu imc é {imc:.2f}""")