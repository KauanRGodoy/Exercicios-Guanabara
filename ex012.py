print('============   DESAFIO 012  ============')
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
n = float(input('Qual o preço do produto? R$'))
# desc 5% = 'o número' - ('o número' * 5/ por 100)
desc = n-(n*5/100)
print('Com 5% de desconto o valor sai por: R${:.2f}'.format(desc))
print('CONCLUIDO!!!')
