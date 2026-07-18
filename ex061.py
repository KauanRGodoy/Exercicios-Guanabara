print('============   DESAFIO 061  ============')
# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('Gerador de PA!')
primeirotermo = int(input('Primeiro termo:'))
razao = int(input('Razão da PA:'))
variaveldotermo = primeirotermo
contador = 1
while contador <= 10:
    print('{} -> '.format(variaveldotermo), end='')
    variaveldotermo += razao
    contador += 1
print('Feito!')
print('CONCLUIDO!!!')