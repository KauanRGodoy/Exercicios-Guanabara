print('============   DESAFIO 027  ============')
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza
# Primeiro= Ana; Ultimo: Souza
nome = str(input('Digite seu nome completo:')).strip()
correcao = nome.lower().title()
quebra = correcao.split()
n1 = quebra[0]
n2 = quebra[len(quebra)-1]
print('Seu primeiro e último nome são: {} {}'.format(n1, n2))
print('CONCLUIDO!!!')
