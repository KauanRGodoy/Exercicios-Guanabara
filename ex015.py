print('============   DESAFIO 015  ============')
# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por KM rodado.
km = int(input('Quantos quilômetros percorridos?'))
dia = int(input('Quantos dias alugados?'))
soma = (dia*60)+(km*0.15)
print('Você rodou {}Km e alugou o veículo por {} dias, o que lhe custará um total de R${:.2f}.'.format(km, dia, soma))
print('CONCLUIDO!!!')
