print('============   DESAFIO 058  ============')
# Melhore o jogo do DESAFIO 28 onde o computador vai 'pensar' em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
sorteador = randint(1, 10)
palpites = 0
print('VAMOS VER SE VOCÊ GANHA DESTA VEZ!\nDigíte um número de 1 a 10')
while True:
    palpites += 1
    print('=======  Vamos para a {}ª rodada!  ======='.format(palpites))
    escolha = int(input('Nº:'))
    if sorteador == escolha:
        print('VOCÊ ACERTOU! PARABENS!')
        print('VOCÊ ERROU {} VEZES E ACERTOU NA {}ª RODADA!!!'.format(palpites - 1, palpites))
        break
    else:
        if sorteador > escolha:
            print('Errou! Mais... Tente novamente!')
        if escolha > sorteador:
                print('Errou! Menos... Tente novamente!')
        print('ERROOOOOU!!! TENTE NOVAMENTE!!!')
print('CONCLUIDO!!!')
