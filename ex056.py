print('============   DESAFIO 056  ============')
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa , mostre: A média de idade do grupo, qual é o nome do homem mais velho, quantas mulheres tem menos de 20 anos.
somaidade = 0
médiaidade = 0
maioridadedohomem = 0
nomehomemmaisvelho = ''
totmulher20 = 0
for pessoa in range(1, 5):
    print('========== {}ª pessoa =========='.format(pessoa))
    nome = str(input('Qual o nome?\n')).strip()
    idade= int(input('Qual a idade?\n'))
    sexo = str(input('Qual o sexo: [M/F]\n')).strip()
    somaidade += idade
    if pessoa == 1 and sexo in 'Mm':
        maioridadedohomem = idade
        nomehomemmaisvelho = nome
    if sexo in 'Mm' and idade > maioridadedohomem:
        maioridadedohomem = idade
        nomehomemmaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
médiaidade = somaidade / 4
print('A média de idade do grupo é de: {}'.format(médiaidade))
print('A idade do homem mais velho é {} e se chame {}.'.format(maioridadedohomem, nomehomemmaisvelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))
print('CONCLUIDO!!!')
