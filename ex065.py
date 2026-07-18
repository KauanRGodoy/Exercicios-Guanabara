print('============   DESAFIO 065  ============')
# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
resp = 'S'
media = quantidade = soma = maior = menor = 0
while resp in 'Ss':
    quantidade += 1
    num = int(input('Digíte o {} número:\n'
                    'N°:'.format(quantidade)))
    soma += num
    if quantidade == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja continuar? [S/N]:\n')).upper().strip()[0]
media = soma / quantidade
print('Você digitou {} números e a média é {}.'.format(quantidade, media))
print('O maior numero foi {} e o menor numero foi {}.'.format(maior, menor))
print('CONCLUIDO!!!')
