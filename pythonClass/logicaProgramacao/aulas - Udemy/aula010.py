#FORMATAÇÃO DE PALAVRAS - FRASES

nome = ... #O valor da variável ainda não foi atribuido por este motivo 3 pontos ( ... )
sobrenome = ...
idade = ...
a = 'NOME 00'
b = 'NOME 01'
c = 1.1
formato = 'a={nome0} b={nome1} c={nome2:.2f}'.format(
    nome0=a,
    nome1=b,
    nome2=c
)

print(formato)
