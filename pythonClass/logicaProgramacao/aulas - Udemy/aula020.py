# FATIAMENTO DE STRINGS
'''

    0123456789
    Mundo olá
    -987654321

    fatiamento [i:f:p] [::]
    
    FUNÇÃO LEN

    A função len retorna a quatidade de caracteres da str

'''
variavel_xis = 'Mundo Olá'

print(variavel_xis)
print(variavel_xis[0])
print(variavel_xis[1])
print(variavel_xis[2])
print(variavel_xis[3])
print(variavel_xis[4])
print(variavel_xis[5])
print(variavel_xis[6])
print(variavel_xis[7])
print(variavel_xis[8])
print(" -------------- ")

print(variavel_xis[-1])
print(variavel_xis[-2])
print(variavel_xis[-3])
print(variavel_xis[-4])
print(variavel_xis[-5])
print(variavel_xis[-6])
print(variavel_xis[-7])
print(variavel_xis[-8])
print(variavel_xis[-9])

print(" -------------- ")

#FATIAMENTO

print(variavel_xis[4:])
print(variavel_xis[6:])
print(variavel_xis[0:5])
print(variavel_xis[-9:-1])
print(" -------------- ")
print(f'A string STR tem [ {len(variavel_xis)} ] letras incluindo o espaço!')
print(" -------------- ")
print(" -------------- ")
print(' ')

print(variavel_xis[0:len(variavel_xis):1]) # Um a Um
print(variavel_xis[0:len(variavel_xis):2]) # Dois em Dois
print(variavel_xis[0:len(variavel_xis):3]) # Três em Três

print(variavel_xis[::-1]) # Um a Um
print(variavel_xis[-1:-10:-2]) # Dois em Dois
print(variavel_xis[-1:-10:-3]) # Três em Três

print(variavel_xis[:1])

