"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 61  # velocidade atual do carro
local_carro = 99  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega
RANGE_MIN_1 = LOCAL_1 - RADAR_RANGE
RANGE_MAX_1 = LOCAL_1 + RADAR_RANGE

in_range = RANGE_MIN_1 <= local_carro <= RANGE_MAX_1
velocidade_permitida = velocidade < RADAR_1

if in_range and (not velocidade_permitida):
    print('multa')
else:
    print('sem multa')