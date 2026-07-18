print('============   DESAFIO 046  ============')
# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifícios, indo de 10 até 0 , com uma pausa de 1 segundo entre eles.
from time import sleep
print('CONTAGEM REGRESSIVA PARA A VIRADA DO ANO!!!')

for fogos in range(10, -1, -1):
    print(str(fogos))
    sleep(1)
print('✨✨✨🎇🎇🎇🎇\n🎆🎆🎆🎆🧨\n🧨🎇🎊🎊🎉🎉\n🎉✨\n✨🎉🎊🎊✨🧨🎇🎆🎉🎊\n🎉✨🎇')
print('CONCLUIDO!!!')
