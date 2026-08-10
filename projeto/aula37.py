"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos 
escreva "Seu nome é curso"; se tiver entre 5 e 6 letras, escreva " Seu nome é normal";
maior que 6  escreva "Seu nome é muito grande"
"""

primeiro_nome = input("Digite o seu primeiro nome: ")

tamanho_nome = len(primeiro_nome)

nome_curto = tamanho_nome > 1 and tamanho_nome < 5
nome_normal = tamanho_nome > 4 and tamanho_nome < 7
nome_grande = tamanho_nome > 6

if nome_curto:
    print("Seu nome é curto")
elif nome_normal:
    print("Seu nome é normal")
elif nome_grande:
    print("Seu nome é grande")
else:
    print("Isso não é um nome")
