#EXERCÍCIO

'''
Solicite ao usuário:
- Nome
- Idade
Caso nome e idade ok:
    printar
        seu nome
        seu nome invertido
        seu nome contém ou não espaços
        seu nome tem N letras
        a primeira letra de seu nome é
        a última letra de seu nome é
senão:
    printar:
        Campos obrigatórios estão vazios!        
'''


nome = input('Digite o seu nome: ')
print('Digite sua idade')
idade = int(input())

if nome and idade:
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é: {nome[::-1]}')

    if ' ' in nome:
        print("Sim seu nome tem espaço!")
    else:
        print('O seu nome não tem espaços!')
    #--
    print(f'Seu nome tem [ {len(nome)} ] letras!')

    print(f'A primeira letra de seu nopme é {nome[0]}')
    print(f'A última letra de seu nome é: {nome[-1]}')
else:
    print('Existem campos obrigatórios a serem preenchidos!')
#--