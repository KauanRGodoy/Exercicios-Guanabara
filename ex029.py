from random import randint
from time import sleep
print('============   DESAFIO 029  ============')
# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7.00 por cada Km acima do limite.
sorter = randint(10, 160)
print('Um carro está a uma velocidade de {}km/h '.format(sorter))
print('PROCESSANDO...')

sleep(3)

v = int(80)
print('A velocidade da via é {}km/h'.format(v))
sleep(2)
if v < sorter:
    print('-=-' * 22)
    print('VOCÊ FOI MULTADO POR ESTAR ACIMA DA VELOCIDADE DA VIA!!! 😡🤬')
    print('Valor da multa: R${:.2f}'.format((sorter-80)*7))
    print('MENOS {} PONTOS NA CARTEIRA!!!'.format(randint(1, 2)))
    print('-=-' * 22)
else:
    print('-=-' * 15)
    print('Você está dentro da velocidade permitida.\n'
          'Dirija com cuidado, BOA VIAGEM! 😊😁')
    print('-=-' * 15)
print('CONCLUIDO!!!')
