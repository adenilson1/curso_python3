"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""

hora = input("Que horas são  ? ")


try:
    hora_float = float(hora)
    bom_dia = hora_float >= 0 and hora_float < 12
    boa_tarde = hora_float >= 12 and hora_float < 18
    boa_noite = hora_float >= 18 and hora_float < 24

    if bom_dia:
        print("Bom dia")
    elif boa_tarde:
        print("Boa tarde")
    elif boa_noite:
        print("Boa noite")
    else:
        print("Essa hora não existe")
except ValueError:
    print("Erro: isso não é um valor de hora")
