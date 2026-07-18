print('============   DESAFIO 010  ============')
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# CONSIDERE US$=1.00 = R$=3.27
print('Hoje')
real = float(input('Converta reais em dólar. Quantos reias você tem? R$'))
dolar = real/4.95
euro = real/5
print('Reais: R${:.2f}\nDólar: US${:.2f}\nEuro: €{:.2f}'.format(real, dolar, euro))
print('='*15)
print('TUTORIAL')
dolar2 = real/3.27
euro2 = real/5.34
print('Reais: R${:.2f}\nDólar: US${:.2f}\nEuro: €{:.2f}'.format(real, dolar2, euro2))
print('CONCLUIDO!!!')
