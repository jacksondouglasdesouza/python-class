'''
REPETIÇÃO
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira

loop infinito >>>  Quando um código não tem um fim
ex:
    cond = True

    while cond:
        print(1 ...)
        print(2 ...)
        print(3 ...)
        print(oo n x ... n oo)
    #--

'''

# While incorreto com loop infinito!

'''
    while condicao:
        nome = input("Qual o seu nome: ")
        print(f'Seu nome é: {nome}')
    #--
    oo Loop ...
'''


# While Correto

condicao = True
nome = ...

while condicao:
    nome = input("Qual o seu nome: ")
    print(f'Seu nome é: {nome}')
    
    if nome:
        break
    #--
#--

print(f'O nome na variável atual é: {nome}')


contador = 0

while contador < 10:
    print(f'O contador vale: {contador}')
    contador += 1 # >> OU >>  contador = contador + 1
#--

if contador:
    print(f'O Contador na Posição {contador} X 2 = {contador * 2}') 
    #Multiplica ou pode ser assim: [contador *= 2] 
    # << Essa é uma forma de declarar o valor da variável somente
    print(f'O Contador na Posição {contador} / 2 = {contador / 2}') 
    #Divide ou pode ser assim: [contador /= 2] 
    # << Essa é uma forma de declarar o valor da variável somente
    print(f'O Contador na Posição {contador} - 2 = {contador - 2}') 
    #Subtrae ou pode ser assim: [contador -= 2] 
    # << Essa é uma forma de declarar o valor da variável somente
    print(f'O Contador na Posição {contador} + 2 = {contador + 2}') 
    #Adiciona ou pode ser assim: [contador += 2] 
    # << Essa é uma forma de declarar o valor da variável somente
    print(f'O Contador na Posição {contador} ** 2 = {contador ** 2}') 
    #Potencia ou pode ser assim: [contador **= 2] 
    # << Essa é uma forma de declarar o valor da variável somente
#--

jota = 0

while jota < 100:
    jota += 1
    print(f'O valor do Jota é: {jota}')

    if jota > 7 and jota <= 15:
        print(f'Não vou mostrar o : {jota}')
        continue
    #--

    if jota == 48:
        print(f'Contagem finalizada no valor {jota}')
        break
    #--
#--
