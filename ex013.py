print('============   DESAFIO 013  ============')
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com  15% de aumento.
soldo = float(input('Calculando o aumento do seu salário em 15%. Digite o seu salário atual: R$'))
aumento = soldo+(soldo*15/100)
# 15% = 'o número' + ('o número' * 15/ por 100)
print('Seu salário do mês que vem com um aumento de 15% será: R${:.2f}'.format(aumento))
print('CONCLUIDO!!!')
