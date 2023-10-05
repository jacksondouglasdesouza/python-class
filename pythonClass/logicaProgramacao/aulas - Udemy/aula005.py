#Conversão de tipos, coerção
#Type convertion, typecasting, coercion
#ato de converter um tipo em outro
#tipos imutáveis e primitivos:
#str, int, float, bool

#print("1" + 1)
#Istó é impossúvel no Python pois ele é uma linguagem dimâmica do tipo forte!

print("ABCDE" + "FGHIJ")
#Isto é possível, havera uma concatenação de tipos. 


print('1', type('1'))
print(int('1'), type(int('1')))
print(int("50") + 50)
print(float("50") + 50, type(float("50")))

print(bool())
print(bool(''))
print(bool(' '))

print(str(4) + 'STR')

