"""
Calculadora com while
"""

numero_tabuada = input('Digite um numero: ')
operacao = input('Escolha uma das operações (+, - , * , /) : ')

numero = int(numero_tabuada)
resultado = 0
condicao = False
contagem = 1


while condicao != True:

    match  operacao:
        case "+":
            print(f"\nTabuada de Soma de {numero}\n")
            while contagem < 11:
                resultado = numero + contagem
                print(f"{numero} + {contagem} = {resultado}")
                contagem += 1
            condicao = True

        case "-":
            print(f"\nTabuada de Diminuir de {numero}\n")
            while contagem < 11:
                resultado = numero - contagem
                print(f"{numero} - {contagem} = {resultado}")
                contagem += 1
                if resultado == 0:
                    break
            condicao = True

        case "*":
            print(f"\nTabuada de Multiplicação de {numero}\n")
            while contagem < 11:
                resultado = numero * contagem
                print(f"{numero} * {contagem} = {resultado}")
                contagem += 1
            condicao = True

        case "/":
            print(f"\nTabuada de Divisao de {numero}\n")
            while contagem < 11:
                resultado = numero / contagem

                if numero % contagem == 0:
                    print(f"{numero} / {contagem} = {resultado}")
                contagem += 1
            condicao = True
