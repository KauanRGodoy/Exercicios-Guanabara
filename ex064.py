print('============   DESAFIO 064  ============')
# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
n = 1
num = cont = soma = 0
num = int(input('Digíte o {}° número. (CASO QUEIRA PARAR DIGÍTE: 999)\n'
                    'N: '.format(n)))
while num != 999:
    soma += num
    cont += 1
    n += 1
    num = int(input('Digíte o {}° número. (CASO QUEIRA PARAR DIGÍTE: 999)\n'
                    'N: '.format(n)))
print('Foram dígitados {} números e a soma entre eles é {}'.format(cont, soma))
print('CONCLUÍDO!!!')
