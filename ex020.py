from random import shuffle
print('============   DESAFIO 020  ============')
# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
a1 = str(input('Primeiro aluno:'))
a2 = str(input('Segundo aluno:'))
a3 = str(input('Terceiro aluno:'))
a4 = str(input('Quarto aluno:'))
trabalhos = [a1, a2, a3, a4]
shuffle(trabalhos)
print('Entre os alunos {}, {}, {} e {} o sorteio para quem vai apresentar o trabalho em ordem vai ser: {}'.format(a1, a2, a3, a4, trabalhos))
print('CONCLUIDO!!!')
