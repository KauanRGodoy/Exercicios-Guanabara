print('============   DESAFIO 017  ============')
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
import math
'''ang = int(input('Digite o valor do ângulo do triângulo retângulo:'))'''
print('------------------------------------------------------------------')
print('MODELO TRADICIONAL')
catop = float(input('Quanto mede o cateto oposto?'))
catad = float(input('Quanto mede o cateto adjacente?'))
hip = (catop**2+catad**2)**(1/2)
print('Para se ter um ângulo de 90°, a hipotenusa vai medir {:.3f}'. format(hip))
print('------------------------------------------------------------------')
print('MODELO IMPORTANDO O MATH')
import math
''' ou from math impor hypot'''
catop = float(input('Quanto mede o cateto oposto?'))
catad = float(input('Quanto mede o cateto adjacente?'))
hi = math.hypot(catop, catad)
print('Para se ter um ângulo de 90°, a hipotenusa vai medir {:.3f}'. format(hi))
print('------------------------------------------------------------------')
print('CONCLUIDO!!!')

