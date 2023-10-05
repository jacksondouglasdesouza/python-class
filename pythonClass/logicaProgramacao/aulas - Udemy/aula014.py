#Operadores de Comparação!

#RELACIONAIS

# OP --------- SIGNIFICADO ---------- EXEMPLO (TRUE OR FALSE)
#  > --------- Maior que  ----------- 20 > 19 ? True
#  >= -------- Maior ou Igual que --- 250 >= 250 ? True
#  < --------- Menor que ------------ 300 < 233  ? False
#  <= -------- Menor ou Igual que --- 350 <= 350 ? True
#  == -------- Igual á -------------- 'Abacate' == 'Abacate' ? True
#. != -------- Diferente de --------- '1' != 1 ? True

maior = 20 > 19
maior_igual = 250 >= 250
menor = 300 < 233
menor_igual =  350 <= 350
igual = 'Abacate' == 'Abacate'
diferente = '1' != '1'

print(f"[ 20 > 19 ] >>> É Maior que? {maior}")
print(f"[ 250 >= 250 ] >>> É Maior ou Igual a? {maior_igual}")
print(f"[ 300 < 233 ] >>> É Menor que?  {menor}")
print(f"[ 350 <= 350 ] >>> É Menor ou Igual? {menor_igual}")
print(f"[ 'Abacate' == 'Abacate' ] >>> É Igual à {igual}")
print(f"[ '1' != '1' ] >>> É Diferente de? {diferente}")


