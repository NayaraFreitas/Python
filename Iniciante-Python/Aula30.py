"""
CONSTANTE = "Variaveis" que não vão mudar
# no python não existe de constante não pode mudar de valor , mas se colocado em letras Maiusculas , para que outros dev identificam que são constante assim  diferencia o tipo de variaveis que não mudam

Muitas condições no memso if (ruim)

     <- Contagem de complexidade (ruim) #espaço desnecessaria , o simples e melhor que complexo

"""

velocidade = 61 #velocidade atual do carro
local_carro = 100 #local em que o carro está na estrada

RADAR_1 = 60 # valocidade máxima do radar 1
LOCAL_1 = 100 #local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega 

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and  local_carro <= (LOCAL_1 + RADAR_RANGE) 

carro_multado = carro_passou_radar_1 and vel_carro_pass_radar_1 

if vel_carro_pass_radar_1:
    print('Velocidade carro passou do radar 1')

# a \ barra para sinalizar para o python que tem continuação do código na linha de baixo
if carro_multado:
    print('carro multado em radar 1')

if carro_passou_radar_1:
    print('carro passou radar 1')