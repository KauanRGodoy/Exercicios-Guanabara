print('============   DESAFIO 025  ============')
# Crie um programa que leia o nome de uma pessoa e diga se ela tem o "Silva" no nome.
nome = str(input('Digite um nome:')).strip()
correcao = nome.lower().title()
result = 'Silva'in correcao
print('No nome {}, há "Silva"? {}'.format(correcao, result))
print('CONCLUIDO!!!')
