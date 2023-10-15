value_001 = 'value 001' # Vai armazenar o valor na mesma variável pelo python
value_002 = 'value 001' # Vai armazenar o valor na mesma variável pelo python
value_003 = 'value 003' # Vai armazenar o valor na mesma variável pelo python
print(id(value_001)) #Vai imprimir o endereço da variável na memória
print(id(value_002)) #Vai imprimir o endereço da variável na memória
print(id(value_003)) #Vai imprimir o endereço na variável diferente na memória

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Esta condição True!')
else:
    print('Esta condição False!')
#--

print('Esse valor passou fora do if!')

print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)

#-- 


'''

Flag (Bandeira) - Marca um local
None = Não tem Valor
is e in not -->>   é ou não é um tipo (Valor, identidade e etc...)
id = Identidade da variável, endereço da variável na memória

'''



