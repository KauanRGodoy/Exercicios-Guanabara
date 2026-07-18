print('============   DESAFIO 004  ============')
# Faça um programa que laia algo pelo teclado e mostre na tela o
# seu tipo primitivo e  todas as informações possíveis sobre ele.
#
# print (n.isnumeric()) isnumeric = é numérico?
# print (n.isalpha()) isalpha = é letra?
# print (n.isupper()) isupper = é letras maiusculas?
# print (n.islower()) islower = é letras minusculas?
# print (n.isspace()) isspace = é somente espaços?
# print (n.isalnum()) isalnum = é alfanumérico?
# print (n.istitle()) istitle = está capitalizada?
#
cores = {'limpa': '\033[m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'rosa': '\033[35m',
         'ciano': '\033[36m',
         'cinza': '\033[37m'}

n = input('Digite algo:')
print('{}O tipo primitivo desse valor é:'.format(cores['vermelho']), type(n))
print('{}É um número?'.format(cores['verde']), n.isnumeric())
print('{}É uma letra/palavra?'.format(cores['amarelo']), n.isalpha())
print('{}É maiúsculo?'.format(cores['azul']), n.isupper())
print('{}É minúsculo?'.format(cores['rosa']), n.islower())
print('{}É alfanumérica?'.format(cores['ciano']), n.isalnum())
print('{}Está capitalizada?'.format(cores['cinza']), n.istitle())
print('{}CONCLUIDO!!!'.format(cores['limpa']))
