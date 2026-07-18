print('============   DESAFIO 043  ============')
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso ; Entre 18.5 e 25: Peso ideal ; 25 até 30: Sobrepeso ; 30 até 40: Obesidade ; Acima de 40: Obesidade mórbida
import math
print('-=' * 17)
print('TABELA DE IMCs:\n'
      '18,5 ou abaixo: ABAIXO DO PESO\n'
      '18,5 e 25: PESO IDEAL\n'
      '25 e 30: SOBREPESO\n'
      '30 e 40: OBESIDADE\n'
      '40 e +: OBESIDADE MÓRBIDA')
print('-=' * 17)
print('Vamos calcular seu IMC (Índice de Massa Corporal):')
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
print('-=' * 9)
peso = float(input('Qual seu peso? (Kg)\n'))
print('-=' * 9)
altura = float(input('Qual sua altura? (m)\n'))
print('-=' * 20)
#
calculo = peso / pow(altura, 2)
#
def tabela(calculo):
    if calculo <= 18.5:
        return ('{}Você está abaixo do peso!!!{}'
                .format(cores['amarelo'], cores['limpa']))
    elif 18.6 <= calculo and calculo <= 25:
        return ('{}Você está com o peso ideal!{}'
                .format(cores['verde'], cores['limpa']))
    elif 26 <= calculo and calculo <= 30:
        return ('{}Você está com sobrepeso!!!{}'
                .format(cores['vermelho'], cores['limpa']))
    elif 31 <= calculo and calculo <= 40:
        return ('{}Vocé está obeso!!!{}'
                .format(cores['vermelho'], cores['limpa']))
    elif calculo >= 40:
        return ('{}Vocé esta com OBESIDADE MÓRBIDA!!!{}'
                .format(cores['vermelho'], cores['limpa']))
#
print('Seu IMC é: {:.2f}'.format(calculo))
print(tabela(calculo))
print('-=' * 20)
#
print('CONCLUIDO!!!')
