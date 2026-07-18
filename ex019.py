from random import choice
print('============   DESAFIO 019  ============')
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.
a1 = str(input('Primeiro aluno:'))
a2 = str(input('Segundo aluno:'))
a3 = str(input('Terceito aluno:'))
a4 = str(input('Quarto aluno:'))
lista = [a1, a2, a3, a4]
# Para o Python [] Colchetes serve para criar uma LISTA
escolhido = choice(lista)
print('Entre {}, {}, {}, e {} o sorteado para apagar o quadro foi: {}'.format(a1, a2, a3, a4, escolhido))
print('CONCLUIDO!!!')