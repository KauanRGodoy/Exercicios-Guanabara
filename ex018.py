print('============   DESAFIO 018 ============')
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan
ang = float(input('Digite um ângulo:'))
sen = sin(radians(ang))
print('O ângulo de {} tenho SEN = {:.3f}'.format(ang, sen))
cos = cos(radians(ang))
print('O ângulo de {} tenho COS= {:.3f}'.format(ang, cos))
tan = tan(radians(ang))
print('O ângulo de {} tenho TAN= {:.3f}'.format(ang, tan))
print('CONCLUIDO!!!')