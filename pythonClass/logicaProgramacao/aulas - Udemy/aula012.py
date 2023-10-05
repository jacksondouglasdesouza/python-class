#IF / ELIF ............. / ELSE
#SE / SE NÃO SE ....... / SE NÃO


entrada = input('Você deseja "Entrar" ou "Sair"? ')
points = '****************************************'
if entrada == 'entrar':
    print(f'\n{points}')
    print(' ')
    print("Seja bem vindo, você entrou no sistema! ")
    print(" ")
    print(f'{points}\n')
elif entrada == 'sair':
    print('Você saio do sistema!')
else:
    print('Você não escolheu nenhuma alternativa válida! ') 
#--

