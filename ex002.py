print('============   DESAFIO 002  ============')
# Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
nome = input('Qual é o seu nome?')
cores = {'limpa': '\033[m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'rosa': '\033[35m',
         'ciano': '\033[36m',
         'cinza': '\033[37m'}

print('É um prazer te conhecer meu amigo, {}monstro dos mares{}, '
      '{}Pika da galaxias{}, {}{}{}!'.format(cores['ciano'], cores['limpa'], cores['amarelo']
                                             , cores['limpa'], cores['vermelho'], nome, cores['limpa']))
print('CONCLUIDO!!!')
