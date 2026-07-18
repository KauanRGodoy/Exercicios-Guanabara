print('============   DESAFIO 051  ============')
# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
print('========================================')
print('     10 PRIMEIROS TERMOS DE UMA PA.')
print('========================================')
pa1 = int(input('Primeiro Termo:'))
razao = int(input('Razão:'))
dez = pa1 + (10 - 1) * razao
for c in range(pa1, dez + razao, razao):
    print(c, end=' - ')
print('CONCLUIDO!!!')
