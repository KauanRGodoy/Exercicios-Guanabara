print('============   DESAFIO 059  ============')
# Crie um programa que leia dois valores e mostre um menu na tela: [1] somar; [2] multiplicar; [3] maior; [4] novos números; [5] sair do programa.
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
cores = {'limpa': '\033[m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'rosa': '\033[35m',
         'ciano': '\033[36m',
         'cinza': '\033[37m'}
sair = False
n1 = float(input('Digíte o primeiro Nº:\n'))
n2 = float(input('Digíte o segundo Nº:\n'))
while True:
    print('========  O que deseja fazer?  ========\n'
          'Selecione de acordo com a tabela abaixo.')
    tabela = int(input('======================\n'
                       '[ 1 ] Somar\n'
                       '[ 2 ] Multiplicar\n'
                       '[ 3 ] Maior\n'
                       '[ 4 ] Novos números\n'
                       '[ 5 ] Sair do programa\n'
                       '======================\n'
                       'Nº: '))
    if tabela == 1:
        soma = n1 + n2
        print('{}A soma entre {} + {} = {}{}'.format(cores['verde'], n1, n2, soma, cores['limpa']))
        print('{}-------------------------------\n'
              '| Voltando para as escolhas! |\n'
              '-------------------------------{}'.format(cores['amarelo'], cores['limpa']))
        print('=*=' * 10)
        sleep(3)
    if tabela == 2:
        multi = n1 * n2
        print('{}A multiplicação entre {} e {} = {}{}'.format(cores['verde'], n1, n2, multi, cores['limpa']))
        print('{}-------------------------------\n'
              '| Voltando para as escolhas! |\n'
              '-------------------------------{}'.format(cores['amarelo'], cores['limpa']))
        sleep(3)
    if tabela == 3:
        if n1 > n2:
            print('{}O PRIMEIRO número é maior que o Segundo número!{}'.format(cores['verde'], cores['limpa']))
            print('{}-------------------------------\n'
                  '| Voltando para as escolhas! |\n'
                  '-------------------------------{}'.format(cores['amarelo'], cores['limpa']))
            sleep(3)
        if n2 > n1:
            print('{}O SEGUNDO número é maior que o primeiro número!{}'.format(cores['verde'], cores['limpa']))
            print('{}-------------------------------\n'
                  '| Voltando para as escolhas! |\n'
                  '-------------------------------{}'.format(cores['amarelo'], cores['limpa']))
            sleep(3)
        if n1 == n2:
            print('{}Os números são IGUAIS!{}'.format(cores['verde'], cores['limpa']))
            print('{}-------------------------------\n'
                  '| Voltando para as escolhas! |\n'
                  '-------------------------------{}'.format(cores['amarelo'], cores['limpa']))
            sleep(3)
    if tabela == 4:
        print('Dígite os novos números')
        n1 = float(input('Digíte o primeiro Nº:\n'))
        n2 = float(input('Digíte o segundo Nº:\n'))
    if tabela == 5:
        print('Obrigado! Tchau, tchau!')
        break
print('CONCLUIDO!!!')
