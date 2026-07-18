print('============   DESAFIO 039  ============')
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar, se ja passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
from datetime import date
#
from time import sleep
#
cores = {'limpa': '\033[m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'rosa': '\033[35m',
         'ciano': '\033[36m',
         'cinza': '\033[37m'}
#
print('VAMOS LÁ GUERREIRO! VAMOS VERIFICAR SE VOCÊ JA PODE SERVIR ÀS FORÇAS ARMADAS!!!')
ano = int(input('Qual o ano que você nasceu?\n'))
#
data = date.today()
#
databr = str('{}/{}/{}'.format(data.day, data.month, data.year))
#
somamais = data.year + 18
#
somamenos = data.year - ano
#
idade = somamenos - 18
#
meses = data.month
#
dia = data.day
#
ano = data.year
#
def falta(idade):
    if idade == -1:
        return '1'
    elif idade == -2:
        return '2'
    elif idade == -3:
        return '3'
#
def mes(meses):
    if meses == 1:
        return 'Janeiro'
    elif meses == 2:
        return 'Fevereiro'
    elif meses == 3:
        return 'Março'
    elif meses == 4:
        return 'Abril'
    elif meses == 5:
        return 'Maio'
    elif meses == 6:
        return 'Junho'
    elif meses == 7:
        return 'Julho'
    elif meses == 8:
        return 'Agosto'
    elif meses == 9:
        return 'Setembro'
    elif meses == 10:
        return 'Outubro'
    elif meses == 11:
        return 'Novenbro'
    elif meses == 12:
        return 'Dezembro'
#
print('--' * 16)
print('{}Hoje é dia {} de {} de {}.'.format(cores['verde'], dia, mes(meses), ano))
print('Você tem {} anos.{}'.format(somamenos, cores['limpa']))
print('--' * 16)
#
print('CALCULANDO...')
sleep(2)
#
def alistamento(somamenos):
    if somamenos > 18:
        return ('------------------------------------\n'
                '{}VOCÊ PASSOU DA HORA DE SE ALISTAR!!!{}\n'
                '------------------------------------').format(cores['vermelho'], cores['limpa'])
    elif somamenos == 18 or somamenos == 17:
        return ('----------------------------------------------------------------------------\n'
                '{}ESTÁ NO ANO DE SE ALISTAR! Corra fazer no site{} https://alistamento.eb.mil.br{}\n'
                '----------------------------------------------------------------------------').format(cores['amarelo'], cores['ciano'], cores['limpa'])
    elif somamenos < 18:
        return ('--------------------------------------------------------------------------\n'
                '{}Você ainda não está na idade de se alistar! Faltam {} anos para se alistar!{}\n'
                '--------------------------------------------------------------------------').format(cores['amarelo'], falta(idade), cores['limpa'])
#
print(alistamento(somamenos))
print('CONCLUIDO!!!')
