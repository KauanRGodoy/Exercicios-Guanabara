print('============   DESAFIO 008  ============')
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
n = float(input('Digite um valor em metros:'))
km = n/1000
hm = n/100
dam = n/10
m = n
dm = n*10
cm = n*100
mm = n*1000
print('Este valor tem:\nQuilômetros: {}km\nHectômetros: {}hm\nDecâmetros: {}dam\nMetros: {}m\nDecímetros: {}dm\nCentímetros: {}cm\nMilímetros: {}mm'.format(km, hm, dam, m, dm, cm, mm))
print('CONCLUIDO!!!')
