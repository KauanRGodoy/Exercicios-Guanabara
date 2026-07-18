from time import sleep
print('============   DESAFIO 030  ============')
# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.
num = int(input('Digite um número:'))
print('ESTE NÚMERO É PAR OU IMPAR?!')
result = num % 2
sleep(3)
if result == 0:
    print('-=-'*10)
    print('Este número é PAR!')
    print('-=-' * 10)
else:
    print('-=-' * 10)
    print('Este número é IMPAR!')
    print('-=-' * 10)
print('CONCLUIDO!!!')
