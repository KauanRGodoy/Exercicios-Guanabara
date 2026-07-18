from pygame import mixer
print('============   DESAFIO 021  ============')
# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
parar = input('Enter para parar...')
# Método que consegui reproduzir a musica
print('CONCLUIDO!!!')