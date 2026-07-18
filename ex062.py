print('============   DESAFIO 062  ============')
# Melhore o DESAFIO 061, perguntadno para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

print('Gerador de PA!')
primeirotermo = int(input('Primeiro termo:'))
razao = int(input('Razão da PA:'))
variaveldotermo = primeirotermo
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} -> '.format(variaveldotermo), end='')
        variaveldotermo += razao
        contador += 1
    print('Feito!')
    maistermos = int(input('Quantos termos quer mostrar a mais?'))
print('FIM')
