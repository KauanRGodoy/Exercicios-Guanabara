print('============   DESAFIO 053  ============')
# Crie um programa que  leia uma frase qualquer e diga se é um palíndromo, desconsiderando os espaços.
# Ex: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA
frase = str(input('Dígite uma frase:')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O invérso de "{}" é "{}".'.format(junto, inverso))
if inverso == junto:
    print('É Palíndromo!')
else:
    print('Não é Palíndromo!')
print('CONCLUIDO!!!')
