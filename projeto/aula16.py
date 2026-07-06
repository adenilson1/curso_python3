# if = se
# elif = se nao se
# else = se nao
entrada = input('"Entrada - E" ou "Saída S"? ')

if entrada.upper() == 'E':
    print('Entrada permidida')
elif entrada.upper() == 'S':
    print('Saída do sistema')
else:
    print('Valor inválido')
