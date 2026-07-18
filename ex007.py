print('============   DESAFIO 007  ============')
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.
print('Olá! Eu sou a ajudante pessoal do aluno! Vamos calculas a sua média!')
n1 = float(input('Qual foi a nota da sua primeira prova?'))
n2 = float(input('Qual foi a nota da sua segunda prova?'))
n3 = float(input('Qual foi a nota da sua terceira prova?'))
result = (n1+n2+n3)/3
print('A média de suas notas são: {} + {} + {} = {:.2f}'.format(n1, n2, n3, result))
print('CONCLUIDO!!!')
