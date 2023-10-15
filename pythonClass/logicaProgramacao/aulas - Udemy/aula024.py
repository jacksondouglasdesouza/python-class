'''
DOCUMENTAÇAÕ:
https://docs.python.org/pt-br/3/library/stdtypes.html
Algumas imutáveis que já vimos: str, int, float, bool

'''

string = 'jackson douglas de souza'

'''
if string != 'jackson douglas de souza':
    print('NOME INVÁLIDO!')
else:
    print(string)
#--
'''

# string[3] = 'ABC'
# NÃO VÁLIDO POIS A STRING É IMUTÁVEL

print(string)

#Uníca forma é concaternar a string com o que precisa!
variavel_concatenada = f'{string[:3]}+ABCD & etc...'
print(variavel_concatenada)

#--

print(string.capitalize())
print(string.upper())
print(string.istitle())
print(string.isdigit())
print(string.zfill(27))
