print('============   DESAFIO 041  ============')
# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM ; Até 14 anos: INFANTIL ; Até 19 anos: JUNIOR ; Até 20 anos: SÊNIOR ; Acima: MASTER
from datetime import date
print('Vamos conferir qual categoria você se encaixa!')
#
ano = int(input('Que ano você nasceu?\n'))
#
data = date.today()
#
idade = data.year - ano
#
def categoria(idade):
    if idade <= 9:
        return ('Você tem {} anos e faz parte da categoria MIRIM!').format(idade)
    elif idade <= 14:
        return ('Você tem {} anos e faz parte da categoria INFANTIL!').format(idade)
    elif idade <= 19:
        return ('Você tem {} anos e faz parte da categoria JUNIOR!').format(idade)
    elif idade == 20:
        return ('Você tem {} anos e faz parte da categoria SÊNIOR!').format(idade)
    elif idade > 20:
        return ('Você tem {} anos e faz parte da categoria MASTER!').format(idade)
print(categoria(idade))
#
print('CONCLUIDO!!!')
