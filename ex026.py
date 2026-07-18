print('============   DESAFIO 026  ============')

# Faça um programa que leia uma frase pelo teclado e mostre:
# 1- Quantas vezes aparecem a letra "A"
# 2- Em que posição ela aparece a primeira vez.
# 3- Em que posição ela aparece a última vez.

texto = str(input('Digite uma frase para descobrir quantos "A" contem nela:')).strip()
frase = (texto.upper())
contagem = (frase.count('A'))
findini = (frase.find('A')+1)
findend = (frase.rfind('A')+1)
print('Na frase escolhida a letra "A" aparece {} vezes, com a primeira aparecendo na casa {} e a última na casa {}.'
      .format(contagem, findini, findend))
print('CONCLUIDO!!!')
