print('============   DESAFIO 040  ============')
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida.
# Média abaixo de 5.0: REPROVADO ; Média entre 5.0 e 6.9: RECUPERAÇÃO ; Média 7.0 ou superior: APROVADO

num1 = float(input('Digíte a sua primeria nota:'))
num2 = float(input('Digíte a sua segunda nota:'))
num3 = float(input('Digíte a sua terceira nota:'))
div = ((num1 + num2 + num3) / 3)

def calc(div):
    if div <= 5:
        return ('REPROVADO! NOTA ABAIXO DA MÉDIA!\n'
                'Sua nota: {:.1f}').format(div)

    elif div <= 6.9:
        return ('RECUPERAÇÃO! SUA NOTA FICOU ENTRE 5.0 E 6.9\n'
                'Sua nota: {:.1f}').format(div)

    elif div >= 7:
        return ('APROVADO! PARABÉNS SUA NOTA FOI BOA!\n'
                'Sua nota: {:.1f}').format(div)
print(calc(div))
print('CONCLUIDO!!!')
