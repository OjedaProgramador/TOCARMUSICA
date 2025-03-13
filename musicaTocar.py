import pygame

res = str(input('Quer ouvir uma boa musica agora: [SIM/NÃO]: ')).strip().upper()
if res == 'SIM':
    escolha = str(input('Qual música --> Amigos tão fiéis; --> Cara de golpe ')).strip().upper()
    if escolha == 'AMIGOS':
        pygame.init()
        pygame.mixer.music.load('pkon_T_002.wav')
        pygame.mixer.music.play()
        pygame.event.wait()
        input()

    elif escolha == 'CARA':
        pygame.init()
        pygame.mixer.music.load('Cara-de-Golpe.wav')
        pygame.mixer.music.play()
        pygame.event.wait()
        input()

else:
    print('Poderá ouvi-lá em outra ocasião')

