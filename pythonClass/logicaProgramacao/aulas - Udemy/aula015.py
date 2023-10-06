#OPERADORES LÓGICOS

# and(e) our (ou) not(não)
# and = Todas as condições devem ser verdadeiras.
# our = Basta um valor verdadeiro entre ambos, para se tornar verdadeiro.
# not = Oposto de True = False; Oposto de False = True
# Nome <<< Não necessáriamente é um tipo lógico mais significa que aquela atribuição a algo não
# não representa um valor.

a = None
print(type(a))
# <class 'NoneType'>
points = "***********************"


'''
if 1 and 1:
    print(True and 1 and False)
'''

print("[ E ] Entrar")
print("[ S ] Sair")
entrada = input()


if entrada == 'E':
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
elif entrada == 'S':
    print("Você saio!")
else:
    print("Entrada de Dados inválida!")
#--




