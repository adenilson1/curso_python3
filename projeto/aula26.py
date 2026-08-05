"""
Formatação básica de strings
s - string
d - int
f - float
.<número de digitos>f
x ou X - Hexadecimal
> - Esquerda
< - Direita
^ - Centro
= - Força o numero aparecer antes do zero
Sinal - + ou -
Ex.: 0 > -100, .1f
Conversion flags - !r !s !a
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}.')
print(f'{variavel: <10}.')
print(f'{variavel:$^10}.')
print(f'{variavel:0^10}.')
print(f'{variavel:*^10}.')
print(f'{variavel:/^10}.')
print(f'{1000.123456789987654321}')
print(f'{1000.123456789987654321:.1f}')
print(f'{1000.123456789987654321:.2f}')
print(f'{1000.123456789987654321:,.1f}')
print(f'{1000.123456789987654321:,.2f}')
print(f'{-1000.123456789987654321:+,.1f}')
print(f'{-1000.123456789987654321:-,.1f}')
print(f'{1000.123456789987654321:0>+10,.1f}')
print(f'{1000.123456789987654321:0=+10,.1f}')
print(f'O Hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')
