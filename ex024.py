print('============   DESAFIO 024  ============')
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"
name = str(input('Digite o nome de uma cidade:')).strip()
lower = name.lower().title()
split = lower.split()
result = 'Santo'in split[0]
print('A cidade começa com o primeiro nome "Santo"? {}'.format(result))
print('========================================================================================')
print(lower[:5] == 'Santo')
print('CONCLUIDO!!!')
