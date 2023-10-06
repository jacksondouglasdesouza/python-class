#Operadores in e not in
# Strings em Python são iteráveis

# --------------------------
# 0| 1 | 2 | 3  | 4  | 5 | 6 |
# j| a | c | k  | s  | o | n |
#-7|-6 |-5 |-4 |-3 |-2 |-1 |
# --------------------------

nome = 'Jackson'
print(nome[0])
print(nome[1])
print(nome[2])
print(nome[3])
print(nome[4])
print(nome[5])
print(nome[6])
print(" ")
print(nome[-1])
print(nome[-2])
print(nome[-3])
print(nome[-4])
print(nome[-5])
print(nome[-6])
print(nome[-7])

print(10 * "*")
print('kson' in nome)
print('kkson' in nome)
print('JACKsoN' in nome) # 

print('Digite o seu nome: ')
nome = input()
print("Digite o que buscar: ")
buscar = input()

if buscar in nome:
    print(f'O intem {buscar} buscado está em {nome}')
else:
    print(f'O intem {buscar} buscado não está em {nome}')
#--
