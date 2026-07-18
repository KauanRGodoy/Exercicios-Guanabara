print('============   DESAFIO 023  ============')
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
# Ex: Digite um número
# Unidade: 4;Dezena: 3;Centena: 8;Milhar: 1
'''num = int(input('Digite um número de 0 a 9999:'))
n = str(num)
m = (n[0])
c = (n[1])
d = (n[2])
u = (n[3])
print('Milhar: {}\n'
      'Centena: {}\n'
      'Dezena: {}\n'
      'Unidade: {}'.format(m, c, d, u))
print('==========================================================================')'''
print('FORMA MATEMÁTICA')
n = int(input('Digite um número de 0 a 9999:'))
m = n // 1000 % 10
c = n // 100 % 10
d = n // 10 % 10
u = n // 1 % 10
print('Milhar: {}\n'
      'Centena: {}\n'
      'Dezena: {}\n'
      'Unidade: {}'.format(m, c, d, u))
print('CONCLUIDO!!!')
