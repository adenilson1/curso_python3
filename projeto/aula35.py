"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou impar. Caso o usuáro não digite um número 
inteiro, informe que não é um número inteiro
"""
# Resulução

numero = input("Digite um número interio: ")

try:
    numero_int = int(numero)
    if numero_int % 2 == 0:
        print(f"{numero_int} é par")
    else:
        print(f"{numero_int} é impar")
except ValueError:
    print("Erro: voce não digitou um número inteiro")
