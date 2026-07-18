print('============   DESAFIO 016  ============')
# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Exeplo: Digite um número: 6.127 O número 6.127 tem a parte inteira 6.
from math import trunc
n = float(input('Digite um número real/com vírgula:'))
inteira = trunc(n)
print('O número {} tem a parte inteira {}. 😊'.format(n, inteira))
print('CONCLUIDO!!!')
