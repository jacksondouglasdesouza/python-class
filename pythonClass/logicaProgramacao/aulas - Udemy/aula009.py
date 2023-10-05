#Ordem precedência

'''
( )	 ->>>>> arênteses	De dentro para fora
** ->>>>> Potenciação 
*  /  %	 ->>>> Multiplicativo	Da esquerda para a direita
+  –	->>>>> Aditivo	Da esquerda para a direita

'''

'''
Quando uma expressão contém mais de um operador, a ordem da avaliação depende da ordem das operações. Para operadores matemáticos, o Python segue a convenção matemática. O acrônimo PEMDAS pode ser útil para lembrar das regras:

Os Parênteses têm a precedência mais alta e podem ser usados para forçar a avaliação de uma expressão na ordem que você quiser. Como as expressões em parênteses são avaliadas primeiro, 2 * (3-1) é 4, e (1+1)**(5-2) é 8. Também é possível usar parênteses para facilitar a leitura de uma expressão, como no caso de (minute * 100) / 60, mesmo se o resultado não for alterado.

A Exponenciação tem a próxima precedência mais alta, então 1 + 2**3 é 9, não 27, e 2 * 3**2 é 18, não 36.

A Multiplicação e a Divisão têm precedência mais alta que a Adição e a Subtração. Assim, 2 * 3 - 1 é 5, não 4, e 6 + 4 / 2 é 8, não 5.

Os operadores com a mesma precedência são avaliados da esquerda para a direita (exceto na exponenciação). Assim, na expressão degrees / 2 * pi, a divisão acontece primeiro e o resultado é multiplicado por pi. Para dividir por 2π, você pode usar parênteses ou escrever degrees / 2 / pi.

Eu não fico sempre tentando lembrar da precedência de operadores. Se a expressão não estiver clara à primeira vista, uso parênteses para fazer isso.


'''

print(1 + 2**3) # 9, não 27
print(2 * 3**2) #é 18, não 36

print(10 / 2 * 3.14151617) #Divisão veio primeiro

print(2 * 3 - 1) #é 5, não 4
print(6 + 4 / 2) #é 8, não 5

print(2 * 10 / (32 ** 2) / 2 + 25) # (32 ** 2)
print(2 * 10 / 1024 / 2 + 25) # 2 * 10
print(100 / 1024 / 2 + 25) # 100 / 1024
print(0.09765625 / 2 + 25) # 0.09765625 / 2
print(0.048828125 + 25) # Final

#print(2 * 10 / (32 ** 2 * (32 ** 2)) / 2 + 25)

x = 18
y = 3

if 4 * y > x - 1:
	print("echo")
elif 2 * x < y:
	print("dot")
elif y > x -10:
	print("echo dot")
else:
	print("dot echo")


print(" ... ")

print(2 ** 4)
print(9 ** 0.5)
print(9 % 2)
print(9 /2)
print(9 // 2)

print(" CONT ....")
cont = 1
while cont < 8:
	if cont < 5:
		print(cont + 2)
	else:
		print(cont - 1)
	cont += 1
# --- 


soma = 0

for cont in range(1, 10, 2):
	soma += cont
	print("Contador = ",cont)
print("Soma = ", soma)


print("CONTINUE ...")

a = 23 - 25 / 5 + 3 * 4
b = ( 17 - 9 ) * 3 / 4 - 10

print(a + b)
print(2 * b - a)

