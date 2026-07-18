from time import sleep
from random import randint
print('============   DESAFIO 028  ============')
# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa devera escrever na tela se o usuário venceu ou perdeu.
print('VAMOS VER SE VOCÊ ADIVINHA O NÚMERO DE 1 A 5 QUE VOU PENSAR!')
n = int(input('Digite o numero de 1 a 5:'))
sorter = randint(1, 5)
sleep(3)
if sorter == n:
    print('PARABENS! VOCÊ ACERTOU! VOCÊ PENSA COMO UM COMPUTADOR!!!')
else:
    print('ERROOOOU!!! TENTE NOVAMENTE, "MERO HUMANO"!')
print('Eu pensei no número: {}'.format(sorter))
print('CONCLUIDO!!!')
