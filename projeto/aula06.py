print(1 + 1)
print('a' + 'b')
# print('1' + 1) # nao se pode concatenar um str com int
print('1', type('1'))
print(int('1'), type(int('1'))) # fez coerção do str para int
print(int('1') + 1) # fez coerção do str para int
print(float('1.2') + 1) # fez coerção do str para float
print(type(float('1.2') + 1)) # fez coerção do str para float
print(bool(' ')) # fez coerção do str para bool
print(str(11) + 'b') # fez coerção do int para str