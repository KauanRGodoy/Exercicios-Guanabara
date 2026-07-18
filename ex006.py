print('============   DESAFIO 006  ============')
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
cores = {'limpa': '\033[m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'rosa': '\033[35m',
         'ciano': '\033[36m',
         'cinza': '\033[37m'}

n1 = int(input('Digite um número:'))
print('{}O número é: {}\n'
      '{}O dobro deste número é: {}\n'
      '{}O triplo deste número é: {}\n'
      '{}A raiz quadrada deste número é: {:.3f}'
      .format(cores['verde'], n1, cores['azul'], n1*2, cores['ciano'], n1*3, cores['rosa'], n1**(1/2)))
print('{}CONCLUIDO!!!'.format(cores['limpa']))