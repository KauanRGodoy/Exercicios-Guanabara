print('============   DESAFIO 035  ============')
# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('-=-' * 20)
print('Vamos ver se os segmentos formam um triângulo?!')
print('-=-' * 20)
a = float(input('Digíte o primeiro segmento:'))
b = float(input('Digíte o segundo segmento:'))
c = float(input('Digíte o terceiro segmento:'))
if a < b + c and b < a + c and c < a + c:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
    print('-=-' * 20)
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')
    print('-=-' * 20)
print('CONCLUIDO!!!')
