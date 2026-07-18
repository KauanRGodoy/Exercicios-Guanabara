print('============   DESAFIO 031  ============')
# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de até 200Km e R$0.45 para viagens mais longas.
from time import sleep
ferias = str(input('Você pegou férias e pode viajar.Vamos calcular o preço da passagem até seu destino. Para onde você vai?')).strip()
local = ferias.lower().title()
distance = int(input('Quantos quilômetros até, {}?'.format(local)))
sleep(2)
if distance <= 200:
    km1 = distance*0.50
    print('-=-'*20)
    print('O preço da passagem é R$0.50 por Km.')
    print('Até {}, irá lhe custar: R${:.2f}'.format(local, km1))
    print('-=-' * 20)
else:
    km2 = distance*0.45
    print('-=-' * 20)
    print('O preço da passagem é R$0.45 por Km.')
    print('Até {}, irá lhe custar: R${:.2f}'.format(local, km2))
    print('-=-' * 20)
print('CONCLUIDO!!!')
