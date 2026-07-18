print('============   DESAFIO 011  ============')
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-lo, sabendo que cada litro de tinta, pinta uma área de 2m².
larg = float(input('Quantos metros de largura tem a parede?'))
alt = float(input('Quantos metros de altura tem a parede?'))
area = larg*alt
lit = (area/2)
print('A área deste cômodo tem: {}m².\nIrá precisar de {:.2f} litros de tinta para pintar.'.format(area, lit))
print('CONCLUIDO!!!')
