#OR

#Avaliação de Curto Circuito:

print(True and False)
print(True and True)
print(False and False and True)
print(False and False and False)
print(' ')
print(True or True)
print(False or True)
print(False or True or False)
print(True or True or False)
print(False or False)
print(False or 0 or True)
print(False or 0 or False or 'VERDADEIRO')
print(False or 0 or False or 1)

senha_digitada = input('Digite sua senha: ') or 'Senha não digitada'
print(senha_digitada)


points = "***********************"


print("[ E ] Entrar")
print("[ S ] Sair")
entrada = input()

if entrada == 'E' or entrada == 'e':
    senha_usuario = 123456789
    bda_user = 123456789
    print("Digite sua senha: ")
    senha = float(input())
    #--
    if senha == senha_usuario and senha == bda_user:
        print(points)
        print("\nBem vindo!")
        print("Você está logado no sistema!\n")
        print(points)
    #--
elif entrada == 'S' or entrada == 's':
    print("Você saio!")
else:
    print("Entrada de Dados inválida!")
#--
