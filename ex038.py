print('============   DESAFIO 038  ============')
# Escreva um programa que leia DOIS NÚMEROS inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro número é maior, o segundo número é maior, não existe valor maior, os dois são iguais.

cores = {'limpa': '\033[m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'rosa': '\033[35m',
         'ciano': '\033[36m',
         'cinza': '\033[37m'}

num1 = int(input('{}Digíte o primeiro número.\n'
                 'N°:'.format(cores ['verde'])))
num2 = int(input('{}Digíte o segundo número.\n'
                 'N°:{}'.format(cores ['verde'], cores ['limpa'])))
from time import sleep
print('CALCULANDO...'), sleep(1.5)
print('-=' * 25)
def maiormenor(num1, num2):
    if num1 > num2:
        return ('{}O primeiro número é maior que o segundo!'.format(cores['azul']))
    elif num1 < num2:
        return ('{}O segundo número é maior que o primeiro!'.format(cores['ciano']))
    elif num1 == num2:
        return ('{}Não existe valor maior, os dois números são iguais!'.format(cores['vermelho']))

print(maiormenor(num1, num2))
print('{}-='.format(cores['limpa']) * 25)
print('CONCLUIDO!!!')
