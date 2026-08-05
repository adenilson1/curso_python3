"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nomee e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Se nome contém (ou não) espços
        Seu tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Descupe, você deixou campos vazios"
"""

# Resolução:
nome = input('Digite o seu nome: ')
idade_str = input('Digite sua idade : ')
espaco_no_nome = False

if nome == '':
    print('Descupe, você deixou campos vazios')
else:

    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é: {nome[::-1]}')

    for i in range(len(nome)):
        if nome[i] == ' ':
            espaco_no_nome = True
    if espaco_no_nome == True:
        print(f'{nome}: contém espaços')

    else:
        print(f'{nome}: não contém espaços')

    print(f'Seu nome {nome} tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome {nome[len(nome) - 1]}')

    if nome == '' or idade_str == '':
        print('Descupe, você deixou campos vazios')
