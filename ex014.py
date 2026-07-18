print('============   DESAFIO 014  ============')
#Escreva um programa que converta uma temperatura digitada em °C e converta para °F.
c = float(input('Qual a temperatura em °C?'))
f = ((c*9)/5)+32
k = c+273.15
print('A temperatura de {}°C em °F fica, {:.2f}°F e em °K, fica {:.2f}°K.'.format(c, f, k))
print('CONCLUIDO!!!')