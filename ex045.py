print('============   DESAFIO 045  ============')
# Crie um programa que faça o computador jogar JOKENPÔ com você
from random import randint
from time import sleep
cores = {'limpa': '\033[m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'rosa': '\033[35m',
         'ciano': '\033[36m',
         'cinza': '\033[37m'}
print('VAMOS VER SE VOCÊ É MELHOR QUE O COMPUTADOR!!!')
escolha = int(input('Vamos jogar PEDRA, PAPEL, TESOURA!\n'
              'Escolha uma das três opções:\n'
              '{}______________\n'
              '| [0] Pedra   |\n'    
              '| [1] Papel   |\n'
              '| [2] Tesoura |\n'
              '--------------{}\n'
              ':'.format(cores['amarelo'], cores['limpa'])))
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)


# Frase V
sleep(1)
print('-=-' * 3)
print('PEDRA!')
sleep(1)
print('PAPEL!')
sleep(1)
print('TESOURA!')
sleep(0.5)
print('-=-' * 3)
# Frase ^

if computador == 0: #pedra
    if escolha == 0:
        print('PEDRA, EMPATE!')
    elif escolha == 1:
        print('PAPEL, VOCÊ GANHOU!')
    elif escolha == 2:
        print('TESOURA, PERDEU!')
elif computador == 1: #papel
    if escolha == 0:
        print('PEDRA, PERDEU!')
    elif escolha == 1:
        print('PAPEL, EMPATE!')
    elif escolha == 2:
        print('TESOURA, GANHOU!')
elif computador == 2: #tesoura
    if escolha == 0:
        print('PEDRA, GANHOU!')
    elif escolha == 1:
        print('PAPEL, PERDEU!')
    elif escolha == 2:
        print('TESOURA, EMPATE!')

print('{}COMPUTADOR: {}'.format(cores['azul'], itens[computador]))
print('{}SUA ESCOLHA: {}'.format(cores['rosa'], itens[escolha]))
print('CONCLUIDO!!!')
