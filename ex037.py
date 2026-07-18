print('============   DESAFIO 037  ============')
# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a BASE DE CONVERSÃO:
# 1 para binário, 2 para octal, 3 para hexadecimal

cores = {'limpa': '\033[m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'rosa': '\033[35m',
         'ciano': '\033[36m',
         'cinza': '\033[37m'}

num = int(input('Digíte um número e após escolha a base de conversão desejada:\n'))

base = int(input('{}Digíte o número de acordo com cada base de conversão!\n'
                 '{}1 - Binário\n'
                 '{}2 - Octal\n'
                 '{}3 - Hexadecimal{}\n'
                 'N°:'.format(cores['verde'], cores['rosa'], cores['amarelo'], cores['azul'], cores['limpa'])))

print('--' * 15)

def escolha(num, base):
    if base == 1:
        return print('{}Em BINÁRIO o número {} é:\n{}'.format(cores['rosa'], num, bin(num)[2:]))
    elif base == 2:
        return print('{}Em OCTAL o número {} é:\n{}'.format(cores['rosa'], num, oct(num)[2:]))
    elif base == 3:
        return print('{}Em HEXADECIMAL o número {} é:\n{}{}'.format(cores['rosa'], num, hex(num)[2:], cores['limpa']))
    else:
        return print('Opção Inválida')
escolha(num, base)


