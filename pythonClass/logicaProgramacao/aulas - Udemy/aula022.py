# CONSTANTES
# Em python não temos constantes, mais por conversão, usasse o nome
# da variável com letras maiúsculas ---> MINHA_CONS_01, MINHA_CONS_02 e etc...
# Nesse sentido, outros programadores do projeto entenderão que:
# Este valor não deve ser alterado por se tratar de um valor fixo, pré estabelecido.
# 
# Dica: Evite usar muitos and, or, not dentro do bloco if, eli, pois o código
# fica muito completo e inelegível em alguns casos.

#EXEMPLO:



velocidade_atual_carro = 79 # velocidade atual do carro  | vc  <-- dininuindo variável
local_carro_se_encontra = 180 # Local que o carro se encontra na estrada em Km  | lc <-- dininuindo variável

VELOCIDADE_MAXIMA_RADAR_1 = 80 # velocidade máxima do radar | VMR_01  <-- dininuindo variável
LOCAL_RADAR_1 = 100 # local onde o radar 1 está KM | LR_01  <-- dininuindo variável
RADAR_RANGE = 1 # a distância onde o radar funciona | RANGE  <-- dininuindo variável


# < atribuir os valores coletados para novas variáveis para uma melhor legibilidade >

#########################################
vc = velocidade_atual_carro            ##
lc = local_carro_se_encontra           ##
VMR_01 = VELOCIDADE_MAXIMA_RADAR_1     ##
LR_01 = LOCAL_RADAR_1                  ##
#############################################################
                                                            #
if vc <= VMR_01 and lc >= LR_01 + 1: # abreviaturas Acima   ^
    print(f'Velecidade de {vc:.2f} km/h.')
    print('Não foi multado. Está dentro dos padrões.')
    #--

elif vc > VMR_01 and lc >= LR_01 + 1:
        print(f'Velecidade de {vc:.2f} km/h.')
        print('Foi multado. Está acima dos padrões.')
        #--

else:
    print('ERRO! Algum problema nos sensores!')
#--
