print('============   DESAFIO 001  ============')
# Crie um programa que escreva "Olá, mundpo!" na tela.
cores = {'limpa': '\033[m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'rosa': '\033[35m',
         'ciano': '\033[36m',
         'cinza': '\033[37m'}

print('{}Olá, Mundo!{}'.format(cores['rosa'], cores['limpa']))
print('CONCLUIDO!!!')
