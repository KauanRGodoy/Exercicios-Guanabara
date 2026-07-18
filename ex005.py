print('============   DESAFIO 005  ============')
# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
cores = {'limpa': '\033[m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'rosa': '\033[35m',
         'ciano': '\033[36m',
         'cinza': '\033[37m'}

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
m = n1*n2
print('{}A multiplicação entre: {} * {} : {}.'
      '\n{}O sucessor de {} é: {}'
      '\n{}O antecessor de {} é: {}'.format(cores['verde'], n1, n2, m, cores['azul'], m, m+1, cores['ciano'], m, m-1))
print('{}CONCLUIDO!!!'.format(cores['limpa']))
