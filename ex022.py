print('============   DESAFIO 022  ============')
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1- O nome com todas as letra maiúsculas
# 2- O nome com todas minúsculas
# 3- Quantas letras ao todo (sem considerar espaços)
# 4- Quantas letras tem o primeiro nome
nome = str(input('Digite seu nome completo:')).strip()
upper = nome.upper()
lower = nome.lower()
split = nome.split()
semesp = len(''.join(split))
pnome = len(split[0])
'''pnome = nome.split(nome[0]).count'''
print('Seu nome completo com todas maiúsculas: {}\n'
      'Seu nome completo com todas minúsculas: {}\n'
      'Quantas letras seu nome tem sem os espaços: {}\n'
      'Quantas letras tem o seu primeiro nome: {}\n'.format(upper, lower, semesp, pnome))
print('CONCLUIDO!!!')
