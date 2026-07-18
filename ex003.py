print('============   DESAFIO 003  ============')
# Crie um programa que leia dois números e mostre a soma entre eles.
cores = {'limpa': '\033[m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'rosa': '\033[35m',
         'ciano': '\033[36m',
         'cinza': '\033[37m'}

n1 = float(input('Digite um número:'))
n2 = float(input('Digite mais um número:'))
s1 = n1+n2
s2 = n1-n2
s3 = n1*n2
print('{}A soma entre {} + {} = {}'.format(cores['verde'], n1, n2, s1))
#
print('{}A subtração entre: {} - {} = {}'.format(cores['vermelho'], n1, n2, s2))
#
print('{}A multiplicação de: {} * {} = {}'.format(cores['amarelo'], n1, n2, s3))
#
print('{}A divisão entre o primeiro número e o segundo: {}'.format(cores['limpa'], n1//n2))
#
print('A divisão entre o segundo número e o primeiro: {}'.format(n2//n1))
#
print('A raiz quadrada do primeiro número:{}'.format(n1**(1/2)))
#
print('A raiz quadrada do segundo número:{}'.format(n2**(1/2)))
#
print('A potência do primeiro número com o segundo:{}'.format(n1**n2))
#
print('A potência do segundo número com o primeiro:{}'.format(n2**n1))
#
print('{}CONCLUIDO!!!'.format(cores['limpa']))
