"""
Iterando srings com while
"""

nome = input('Digite um nome: ')
tamanho_nome = len(nome)
novo_nome = ''
contador = 0

while contador < tamanho_nome:

    novo_nome += '*' + nome[contador]
    contador += 1

print(nome)
print(novo_nome)
