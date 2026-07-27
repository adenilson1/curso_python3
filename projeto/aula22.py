# Operador lógicos
# and (e) or (ou) not (não)

# or - Qualquer condição verlida, a expressão inteira é verdadeira
# considerado falso, a expressão inteira será avaliada naquele valor.
# São considerações falsas:
# 0 0.0 '' False
# Também existe o tipo None que é usado para representar um não valor

# entrada = input('[E]entrar [S]sair: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

# Avaliação de curto-circuito

print(True and 0 and True)
print(True or 0 or True)
print(0 or False or 0 or 'abc')
senha = input('Senha: ') or 'Sem senha'
print(senha)
