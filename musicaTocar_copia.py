import pygame

res = ''
while res not in 'SN':
    while res not in 'SN':
        res = str(input('Resposta Inválida. Quer ouvir uma boa nusica agora: [SIM/NÃO]: ')).strip().upper()





    if res == 'SIM':
        escolha = str(input('Qual música --> Amigos tão fiéis; --> Cara de golpe ')).strip().upper()
        if escolha == 'AMIGOS':
            print('ouvindo a musica amigos')
            #pygame.init()
            #pygame.mixer.music.load('pkon_T_002.wav')
            #pygame.mixer.music.play()
            ##pygame.event.wait()
            #input()

        elif escolha == 'CARA':
            print('ouvindo a musica cara')
            #pygame.init()
            #pygame.mixer.music.load('Cara-de-Golpe.wav')
            #pygame.mixer.music.play()
            #pygame.event.wait()
            #input()

    else:
        print('Poderá ouvi-lá em outra ocasião')
        break
