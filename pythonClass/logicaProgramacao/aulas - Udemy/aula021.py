#TRY EXCEPT

'''
    Introdução ao try/except

    try:
        tentar executar esse trecho do código
    except:
        ocorreu um erro ao tentar executar este trecho do código
    #--

'''
numero = input('Dobrando o número digitado: ')

# FORMA BÁSICA DE TRY/EXCEPT - APRENDIZADO

try:
    numero_float = float(numero)
    print(f'O número convertido para float é: {numero_float}')
    print(f'O  dobro do número é : {numero_float * 2}')
except:
    print(f'{numero} isso não é um numeral!')
#--
