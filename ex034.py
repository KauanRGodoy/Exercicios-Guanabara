print('============   DESAFIO 034  ============')
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250.00, calcule um aumneto de 10%
# Para os inferiores ou iguais, o aumento é de 15%
x = float(input('Vamos calcular o aumento para você. Qual o valor do seu salário? R$'))
if x <= 1250.00:
    print('15%')
    print('Seu salário vai passar a ser: R${:.2f}'.format(x+(x*15/100)))
else:
    print('10%')
    print('Seu salário vai passar a ser: R${:.2f}'.format(x+(x*10/100)))
print('CONCLUIDO!!!')
