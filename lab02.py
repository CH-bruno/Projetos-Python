###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Chegada na Estação
# Nome: Bruno Cardoso Holanda
# RA: 167542
###################################################

# Leitura de dados
x = int(input()) #distância em quilômetros entre as duas estações 
t = int(input()) #diferença em minutos do tempo de saída dos dois trens 
v_1 = float(input()) #velocidade do trem T1 em km/h 
v_2 = float(input()) #velocidade do trem T2 em km/h

# Cálculo dos tempos de viagem
t1= (x/v_1) - (t/60)
t2= (x/v_2) 


# Impressão da resposta
if t1 > t2 or t1 == t2:
    print(False)
else:
    print(True)
