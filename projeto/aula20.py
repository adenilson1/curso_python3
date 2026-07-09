"""
EXERCÍCIO
"""
print("### PROGRAMA QUE COMPARA DOIS NUMEROS INTEIROS ###\n")

primeiro_valor = input("Digite o primeiro valor: ")
int_primeiro_valor = int(primeiro_valor)

segundo_valor = input("Digite o segundo  valor: ")
int_segundo_valor = int(segundo_valor)

print("\n-----------------------------\n")

# Análise comparativa
if ((int_primeiro_valor > int_segundo_valor) or (int_segundo_valor < int_primeiro_valor)):
    print(
        f"O primeiro valor {int_primeiro_valor} é maior do que o segundo valor {int_segundo_valor}")
elif ((int_segundo_valor > int_primeiro_valor) or (int_primeiro_valor < int_segundo_valor)):
    print(
        f"O segundo valor {int_segundo_valor} é maior do que o primeiro valor {int_primeiro_valor}")
else:
    print(
        f"{int_primeiro_valor} é igual {int_segundo_valor}")

print("\n")
