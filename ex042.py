print('============   DESAFIO 042  ============')
# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais ; Isósceles: Dois lados iguais ; Escaleno: todos os lados diferentes.

print('-=-' * 20)
print('Vamos ver se os segmentos formam um triângulo?!')
print('-=-' * 20)

a = float(input('Digíte o primeiro segmento:'))
b = float(input('Digíte o segundo segmento:'))
c = float(input('Digíte o terceiro segmento:'))

if a < b + c and b < a + c and c < a + c:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if a == b and b == c:
        print('EQUILÁTERO')
    elif a != b and b != c and c != a:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')
print('CONCLUIDO!!!')
