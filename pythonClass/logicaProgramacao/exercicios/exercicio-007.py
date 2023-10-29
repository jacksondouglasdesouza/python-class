#FAÇA UMA CALCULADORA COM WHILE

# >>>  Peça dois valores de entrada
# >>>  Peça um operador
# >>>  Fazer operação e tratamento de possíveis erros
# >>>  Imprimir Resultado ao usuário

#--


while True:

    value_001 = input("Digite o Primeiro Número: ")
    value_002 = input("Digite o Segundo Número: ")
    operador = input("Escolha um operador:\n[+]\n[-]\n[*]\n[/]")

    numeros_validos = None # <<< Flag
    nun_001 = 0
    nun_002 = 0

    try:
        nun_001 = float(value_001)
        nun_002 = float(value_002)
        numeros_validos = True
    except:
        numeros_validos = None
    #--

    if numeros_validos is None:
        print("Algum número digitado é inválido!")
        continue
    #--

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print("Operação escolhida é inválida!")
        continue
    #--

    if len(operador) > 1:
        print('Não é permitido escolher mais de uma Operação por vez!')
        continue
    #--

    # Calcs <<<

    print("Confira o Resultado: ")

    if operador == '+':
        print(f'O resultado de {nun_001:.2f} + {nun_002:.2f} é: {nun_001 + nun_002:.2f}')
    elif operador == '-':
        print(f'O resultado de {nun_001:.2f} - {nun_002:.2f} é: {nun_001 - nun_002:.2f}')
    elif operador == '*':
        print(f'O resultado de {nun_001:.2f} x {nun_002:.2f} é: {nun_001 * nun_002:.2f}')
    elif operador == '/':
        print(f'O resultado de {nun_001:.2f} / {nun_002:.2f} é: {nun_001 / nun_002:.2f}')
    else:
        print(f" ESTRANHO (o_O) ")
        print('Isso não deveria chegar até aqui!')
        print('Vou consultar meu OVNI... Aguarda um minuto!')
    #--
    
    sair = input('Deseja Sair? \n[S] - Sim\n[N] - Não\nDigite:  ').lower().startswith('s')
    if sair is True:
        break
    #--
#--