print('============   DESAFIO 032  ============')
# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
from datetime import date
ano = int(input('Digite um ano para descobrir se ele é bissexto'
                '\nou coloque 0 para saber se o ano atual é bissexto: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    # if/se ano '%'/divisivel 4 == 0, and/e tambem ano '%'/divisivel 100 !=/diferente ou igual a 0, or/ou então ano %/divisivel 400 ==/igual 0
    print('O ano {} é BISSEXTO.'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO.'.format(ano))
print('CONCLUIDO!!!')
