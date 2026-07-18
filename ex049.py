print('============   DESAFIO 049  ============')
# Refaça o desafio 009, mostrando a tabuada de um número que o usuario escolher, só que agora utilizando um laço for
num = int(input('Digíte o número quw deseja ver a tábuada:\n'))
for c in range(1, 11):
    print('{} x {} = {}'.format(num, c, num * c))
print('CONCLUIDO!!!')
