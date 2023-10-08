#INTERPOLAÇÃO

#Interpolação Básica de Strings
# s - string
# d & i - int
# f - float
# x & X - Hexadecimal (0123456789ABCDEF)

nome = 'Jackson Douglas'
preco = 1023.985674325
variavel = '%s, o preço do produto é %.2f' % (nome, preco)
value = 255 ** 10

print(variavel)
print(" ")
print('O Hexadecimal do valor %f é %X \n' % (value, value))

#INTERPOLAÇÃO COM f'STRINGS'

# [ Caracter ] [ (>) ESQUERDA ^CENTRO (^) DIREITA (<) ]

# > - Esquerda
# < - Direita
# ^ - Centro
# = - Força o número a aparecer antes dos zeros
# Sinais de (+) ou (-)
# EX:
# value:0=+10,.2f  ou  -value:-,.2f
#--
# Conversion flags - [ !r ] [ !s ] [ !a ]

value_um = 'ABCD'
print(value_um)

print(f'{value_um: >12}')
print(f'{value_um: <12}')
print(f'{value_um: ^12}')
print("*****************")
print(f'{value_um:0>12}')
print(f'{value_um:0<12}')
print(f'{value_um:0^12}')
print("*****************")
print(f'{value_um:$>12}')
print(f'{value_um:$<12}')
print(f'{value_um:$^12}')
print("*****************")
print("*****************")

print(f'{value:.2f}')
print(f'{value:.4f}')
print(f'{value:,.2f}')
print(f'{-value:,.2f}')
print(f'{-value:-,.2f}')
print(f'{+value:+,.2f}')
print(f'{value:0=+10,.2f}')

value_hexadecimal = 36 ** 3

print(f'O número {value_hexadecimal} em hexadecimal é: {value_hexadecimal:08X}')


#FLAGS

value_flags = 52865.87532145

print(f'Value this : {value_flags!r}')
print(f'Value this : {value_flags!s}')
print(f'Value this : {value_flags!a}')






