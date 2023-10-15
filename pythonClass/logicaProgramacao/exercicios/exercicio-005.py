'''
Exercício 01 - 
Faça um programa que peça ao usuário para digitar um número inteiro, informe se 
este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que esté valor digitado, não é um número inteiro.

'''
print("Digite um número inteiro: ")
value_usuario = input()

#forma VALUE.ISDIGIT()....

if value_usuario.isdigit():
    value = int(value_usuario)
    if value % 2 == 0:
        print(f'O número {value} digitado é par!')
    else:
        print(f'O número {value} digitado é ímpar!')
    #--
else:
    print('O valor de entrada não é um número inteiro!')
#--

# Outra forma com TRY | EXCEPT

try:
    if value_usuario:
        value = int(value_usuario)
        if value % 2 == 0:
            print(f'O número {value} digitado é par!')
        else:
            print(f'O número {value} digitado é ímpar!')
    #--
except:
    print('O valor de entrada não é um número inteiro!')
#--


'''
Exercício 02 - 
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. EX:
Bom dia 00:00h às 11:00h
Boa tarde 12:00h às 17:00h
Boa noite 18:00h às 23:00h

'''

print("Digite o horário: ")
entrada_usuario = input()

try:
    if entrada_usuario:
        value_user = float(entrada_usuario)
        if value_user >= 00.0 and value_user < 12.0:
            print(f"São {value_user} horas - Bom dia!")
        elif value_user >= 12.0 and value_user < 18.0:
            print(f"São {value_user} horas - Boa Tarde!")
        elif value_user >= 18.0 and value_user <= 23.59:
            print(f"São {value_user} horas - Boa Noite!")
        else:
            print(f"Impossível usar este valor {value_user} para horário!")
        #--
    #--
except:
    print('ERROR!')
    print('Dados Inseridos é inválido!')
#--

'''
Exercício 03 - 
Faça um programa que peça o primeiro nome do usuário.
Se o nome tiver 4 letras ou menos, escre: 
Seu nome é curto.
Se tiver entre 5 e 6 letras:
Seu nome é noermal
Else:
Seu nome é multo grande.

'''

nome_usuario = input("Insira o seu nome: ")

if nome_usuario:
    if len(nome_usuario) > 6:
        print(f'Seu nome tem {len(nome_usuario)} letras, ele é muito grande!')
    elif len(nome_usuario) >=5 and len(nome_usuario) <= 6:
        print(f'Seu nome tem {len(nome_usuario)} letras, ele é normal')
    elif len(nome_usuario) <= 4:
        print(f'Seu nome tem {len(nome_usuario)} letras, ele é muito pequeno!')
    #--
else:
    print("ERROR!")
    print(f'O CAMPO NÃO PODE SER VAZIO!')
#--