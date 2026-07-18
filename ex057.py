print('============   DESAFIO 057  ============')
# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digítação novamente até ter um valor correto.
'''
while True:
    nome = str(input('Digíte o nome de uma pessoa:'))
    sexo = str(input('Qual o sexo dessa pessoa? [M/F]')).upper()
    if sexo == 'M':
        print('Esta pessoa é do sexo MASCULINO')
        break
    if sexo == 'F':
        print('Esta pessoa é do sexo FEMININO')
        break
    else:
        print('ESTE SEXO NÃO EXISTE, TENTE NOVAMENTE!')
print('CONCLUIDO!!!')
'''
sexo = str(input('Digíte seu sexo para registro: [M/F]\n:')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('ESTE SEXO NÃO EXISTE, DIGÍTE UM SEXO VÁLIDO: [M/F]\n:')).strip().upper()[0]
print('Este sexo {} foi registrado com sucesso!'.format(sexo))
print('CONCLUIDO!!!')