#NOT

# O operador lógico not é responsável por fazer chexagem de valores e inverter valores de variáveis
# quando acrescentados no código em suas respectivas funções

print(not True)
print(not False)
print(not 1)
print(not 0)

#Exemplo

print('Digite sua senha: ')
senha = input()

if not senha:
    print("Você não digitou sua senha!\n")
#-- 

email = 'exemple@exemple.com'

print('Digite agora o seu email: ')
email_user = input()

if email_user != email:
    print("Seu email está incorreto!\n")
#--

