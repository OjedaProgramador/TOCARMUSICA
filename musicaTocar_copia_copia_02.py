import pygame
while True:
    b = 'SEJAM TODOS MUITO BEM VINDOS'
    print(f'{b:=^50}')
    res = ' '
    while res not in 'SN':
        res = str(input('Quer ouvir uma boa nusica agora: [SIM/NÃO]: ')).strip().upper()[0]
        print('==-' * 25)
    if res == 'N':
        print('FIM DO PROGRAMA')
        break
    print('''Qual Música quer ouvir:\nopção:01 - Amigos tão fiéis\nopção:02 - Cara de golpe   ''')
    escolha = int(input('Qual música:\n 01\n 02\n =  '))
    if escolha == 1:
        print('ouvindo a musica amigos')
        pygame.init()
        pygame.mixer.music.load('pkon_T_002.wav')
        pygame.mixer.music.play()
        input()
        pygame.event.wait()

    elif escolha == 2:
        print('Cara de golpe')
        pygame.init()
        pygame.mixer.music.load('Cara-de-Golpe.wav')
        pygame.mixer.music.play()
        input()
        pygame.event.wait()


    resp = ' '
    while resp not in 'SN':
        resp = str(input('quer continuar [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        print('FIM DO PROGRAMA')
        break
i = 'VOLTEM SEMPRE'
print(f'{i:=^50}')




