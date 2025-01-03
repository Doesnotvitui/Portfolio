'''
Nomes dos integrantes do grupo:
- Leonardo de Goes da Silva
- Nicolas Aparecido Ferreira
- Vithor Augusto Andrade
- Felipe Fernandes Bortolino
- João Victor Repula Cordeiro
'''

import random
import time

print('JOGO DE MATEMATICA')
print('[1] Singleplayer')
print('[2] Multiplayer')
print('')
ask = int(input('Escolha um modo de jogo:'))

#modo singleplayer teste
if(ask == 1):
    print('[1] Fácil (-10 a 10)')
    print('[2] Médio (-100 a 100)')
    print('[3] Díficil (-1000 a 1000)')

    start = int(input('Escolha sua dificuldade:'))
    enter = input('Aperte enter para começar')

    if(start == 1):
        t1 = time.time()

        n1 = random.randint(-10,10)
        n2 = random.randint(-10,10)
        som = n1 + n2
        tasksom = int(input(f'{n1} + {n2} ='))

        n1 = random.randint(-10, 10)
        n2 = random.randint(-10, 10)
        sub = n1 - n2
        tasksub = int(input(f'{n1} - {n2} ='))

        n1 = random.randint(-10, 10)
        n2 = random.randint(-10, 10)
        mult = n1 * n2
        taskmult = int(input(f'{n1} x {n2} ='))

        n1 = random.randint(-10, 10)
        n2 = random.randint(-10, 10)
        div = n1 // n2
        taskdiv = int(input(f'{n1} / {n2} ='))

        t2 = time.time()
        tf = t2 - t1

        #Esquema da pontuação
        if(tasksom == som):
            if (tf > 30):
                print('Tempo esgotado!')
            elif (tf > 5):
                ponto = abs(((tf - 5) * 0.2) - 10)
                pontoSom = ponto
            else:
                pontoSom = 10
        else:
            pontoSom = 0

        if (tasksub == sub):
            if (tf > 30):
                print('Tempo esgotado!')
            elif (tf > 5):
                ponto = abs(((tf - 5) * 0.2) - 10)
                pontoSub = ponto
            else:
                pontoSub = 10
        else:
            pontoSub = 0

        if (taskmult == mult):
            if (tf > 30):
                print('Tempo esgotado!')
            elif (tf > 5):
                ponto = abs(((tf - 5) * 0.2) - 10)
                pontoMult = ponto
            else:
                pontoMult = 10
        else:
            pontoMult = 0

        if (taskdiv == div):
            if (tf > 30):
                print('Tempo esgotado!')
            elif (tf > 5):
                ponto = abs(((tf - 5) * 0.2) - 10)
                pontoDiv = ponto
            else:
                pontoDiv = 10
        else:
            pontoDiv = 0

        pontof = int(pontoSom + pontoSub + pontoMult + pontoDiv)
        if(pontof > 0):
            print(f'Sua pontuação final foi {pontof} pontos. Tempo de jogo:{tf:.2f}s')
        else:
            print('Errou tudo!') #fim do esquema da pontuação

    elif(start == 2):
        t1 = time.time()

        n1 = random.randint(-100, 100)
        n2 = random.randint(-100, 100)
        som = n1 + n2
        tasksom = int(input(f'{n1} + {n2} ='))

        n1 = random.randint(-100, 100)
        n2 = random.randint(-100, 100)
        sub = n1 - n2
        tasksub = int(input(f'{n1} - {n2} ='))

        n1 = random.randint(-100, 100)
        n2 = random.randint(-100, 100)
        mult = n1 * n2
        taskmult = int(input(f'{n1} x {n2} ='))

        n1 = random.randint(-100, 100)
        n2 = random.randint(-100, 100)
        div = n1 // n2
        taskdiv = int(input(f'{n1} / {n2} ='))

        t2 = time.time()
        tf = t2 - t1

        #Esquema da pontuação
        if(tasksom == som):
            if (tf > 30):
                print('Tempo esgotado!')
            elif (tf > 5):
                ponto = abs(((tf - 5) * 0.2) - 10)
                pontoSom = ponto
            else:
                pontoSom = 10
        else:
            pontoSom = 0

        if (tasksub == sub):
            if (tf > 30):
                print('Tempo esgotado!')
            elif (tf > 5):
                ponto = abs(((tf - 5) * 0.2) - 10)
                pontoSub = ponto
            else:
                pontoSub = 10
        else:
            pontoSub = 0

        if (taskmult == mult):
            if (tf > 30):
                print('Tempo esgotado!')
            elif (tf > 5):
                ponto = abs(((tf - 5) * 0.2) - 10)
                pontoMult = ponto
            else:
                pontoMult = 10
        else:
            pontoMult = 0

        if (taskdiv == div):
            if (tf > 30):
                print('Tempo esgotado!')
            elif (tf > 5):
                ponto = abs(((tf - 5) * 0.2) - 10)
                pontoDiv = ponto
            else:
                pontoDiv = 10
        else:
            pontoDiv = 0

        pontof = int(pontoSom + pontoSub + pontoMult + pontoDiv)
        if(pontof > 0):
            print(f'Sua pontuação final foi {pontof} pontos. Tempo de jogo:{tf:.2f}s')
        else:
            print('Errou tudo!') #fim do esquema da pontuação

    elif(start == 3):
        t1 = time.time()

        n1 = random.randint(-1000, 1000)
        n2 = random.randint(-1000, 1000)
        som = n1 + n2
        tasksom = int(input(f'{n1} + {n2} ='))

        n1 = random.randint(-1000, 1000)
        n2 = random.randint(-1000, 1000)
        sub = n1 - n2
        tasksub = int(input(f'{n1} - {n2} ='))

        n1 = random.randint(-1000, 1000)
        n2 = random.randint(-1000, 1000)
        mult = n1 * n2
        taskmult = int(input(f'{n1} x {n2} ='))

        n1 = random.randint(-1000, 1000)
        n2 = random.randint(-1000, 1000)
        div = n1 // n2
        taskdiv = int(input(f'{n1} / {n2} ='))

        t2 = time.time()
        tf = t2 - t1

        #Esquema da pontuação
        if(tasksom == som):
            if (tf > 30):
                print('Tempo esgotado!')
            elif (tf > 5):
                ponto = abs(((tf - 5) * 0.2) - 10)
                pontoSom = ponto
            else:
                pontoSom = 10
        else:
            pontoSom = 0

        if (tasksub == sub):
            if (tf > 30):
                print('Tempo esgotado!')
            elif (tf > 5):
                ponto = abs(((tf - 5) * 0.2) - 10)
                pontoSub = ponto
            else:
                pontoSub = 10
        else:
            pontoSub = 0

        if (taskmult == mult):
            if (tf > 30):
                print('Tempo esgotado!')
            elif (tf > 5):
                ponto = abs(((tf - 5) * 0.2) - 10)
                pontoMult = ponto
            else:
                pontoMult = 10
        else:
            pontoMult = 0

        if (taskdiv == div):
            if (tf > 30):
                print('Tempo esgotado!')
            elif (tf > 5):
                ponto = abs(((tf - 5) * 0.2) - 10)
                pontoDiv = ponto
            else:
                pontoDiv = 10
        else:
            pontoDiv = 0

        pontof = int(pontoSom + pontoSub + pontoMult + pontoDiv)
        if(pontof > 0):
            print(f'Sua pontuação final foi {pontof} pontos. Tempo de jogo:{tf:.2f}s')
        else:
            print('Errou tudo!') #fim do esquema da pontuação

    else:
        print('INVALIDO')

#multijogador teste
elif(ask == 2):
    print('[1] Fácil (-10 a 10)')
    print('[2] Médio (-100 a 100)')
    print('[3] Díficil (-1000 a 1000)')
    print('')
    start = int(input('Escolham sua dificuldade:'))
    enter = input('(PLAYER 1)Aperte enter para começar')

    #PLAYER 1
    if (start == 1):
        t1 = time.time()

        n1 = random.randint(-10, 10)
        n2 = random.randint(-10, 10)
        som = n1 + n2
        tasksom = int(input(f'{n1} + {n2} ='))

        n1 = random.randint(-10, 10)
        n2 = random.randint(-10, 10)
        sub = n1 - n2
        tasksub = int(input(f'{n1} - {n2} ='))

        n1 = random.randint(-10, 10)
        n2 = random.randint(-10, 10)
        mult = n1 * n2
        taskmult = int(input(f'{n1} x {n2} ='))

        n1 = random.randint(-10, 10)
        n2 = random.randint(-10, 10)
        div = n1 // n2
        taskdiv = int(input(f'{n1} / {n2} ='))

        t2 = time.time()
        tf = t2 - t1

        # Esquema da pontuação
        if (tasksom == som):
            if (tf > 30):
                print('Tempo esgotado!')
            elif (tf > 5):
                ponto = abs(((tf - 5) * 0.2) - 10)
                pontoSom = ponto
            else:
                pontoSom = 10
        else:
            pontoSom = 0

        if (tasksub == sub):
            if (tf > 30):
                print('Tempo esgotado!')
            elif (tf > 5):
                ponto = abs(((tf - 5) * 0.2) - 10)
                pontoSub = ponto
            else:
                pontoSub = 10
        else:
            pontoSub = 0

        if (taskmult == mult):
            if (tf > 30):
                print('Tempo esgotado!')
            elif (tf > 5):
                ponto = abs(((tf - 5) * 0.2) - 10)
                pontoMult = ponto
            else:
                pontoMult = 10
        else:
            pontoMult = 0

        if (taskdiv == div):
            if (tf > 30):
                print('Tempo esgotado!')
            elif (tf > 5):
                ponto = abs(((tf - 5) * 0.2) - 10)
                pontoDiv = ponto
            else:
                pontoDiv = 10
        else:
            pontoDiv = 0

        pontoPlayer1 = int(pontoSom + pontoSub + pontoMult + pontoDiv)
        if (pontoPlayer1 > 0):
            print(f'Sua pontuação final foi {pontoPlayer1}. Tempo de Jogo:{tf:.2f}s')
        else:
            print('Errou tudo!')  # fim do esquema da pontuação

    elif (start == 2):
        t1 = time.time()

        n1 = random.randint(-100, 100)
        n2 = random.randint(-100, 100)
        som = n1 + n2
        tasksom = int(input(f'{n1} + {n2} ='))

        n1 = random.randint(-100, 100)
        n2 = random.randint(-100, 100)
        sub = n1 - n2
        tasksub = int(input(f'{n1} - {n2} ='))

        n1 = random.randint(-100, 100)
        n2 = random.randint(-100, 100)
        mult = n1 * n2
        taskmult = int(input(f'{n1} x {n2} ='))

        n1 = random.randint(-100, 100)
        n2 = random.randint(-100, 100)
        div = n1 // n2
        taskdiv = int(input(f'{n1} / {n2} ='))

        t2 = time.time()
        tf = t2 - t1

        # Esquema da pontuação
        if (tasksom == som):
            if (tf > 30):
                print('Tempo esgotado!')
            elif (tf > 5):
                ponto = abs(((tf - 5) * 0.2) - 10)
                pontoSom = ponto
            else:
                pontoSom = 10
        else:
            pontoSom = 0

        if (tasksub == sub):
            if (tf > 30):
                print('Tempo esgotado!')
            elif (tf > 5):
                ponto = abs(((tf - 5) * 0.2) - 10)
                pontoSub = ponto
            else:
                pontoSub = 10
        else:
            pontoSub = 0

        if (taskmult == mult):
            if (tf > 30):
                print('Tempo esgotado!')
            elif (tf > 5):
                ponto = abs(((tf - 5) * 0.2) - 10)
                pontoMult = ponto
            else:
                pontoMult = 10
        else:
            pontoMult = 0

        if (taskdiv == div):
            if (tf > 30):
                print('Tempo esgotado!')
            elif (tf > 5):
                ponto = abs(((tf - 5) * 0.2) - 10)
                pontoDiv = ponto
            else:
                pontoDiv = 10
        else:
            pontoDiv = 0

        pontoPlayer1 = int(pontoSom + pontoSub + pontoMult + pontoDiv)
        if (pontoPlayer1 > 0):
            print(f'Sua pontuação final foi {pontoPlayer1}. Tempo de Jogo:{tf:.2f}s')
        else:
            print('Errou tudo!')  # fim do esquema da pontuação

    elif (start == 3):
        t1 = time.time()

        n1 = random.randint(-1000, 1000)
        n2 = random.randint(-1000, 1000)
        som = n1 + n2
        tasksom = int(input(f'{n1} + {n2} ='))

        n1 = random.randint(-1000, 1000)
        n2 = random.randint(-1000, 1000)
        sub = n1 - n2
        tasksub = int(input(f'{n1} - {n2} ='))

        n1 = random.randint(-1000, 1000)
        n2 = random.randint(-1000, 1000)
        mult = n1 * n2
        taskmult = int(input(f'{n1} x {n2} ='))

        n1 = random.randint(-1000, 1000)
        n2 = random.randint(-1000, 1000)
        div = n1 // n2
        taskdiv = int(input(f'{n1} / {n2} ='))

        t2 = time.time()
        tf = t2 - t1

        # Esquema da pontuação
        if (tasksom == som):
            if (tf > 30):
                print('Tempo esgotado!')
            elif (tf > 5):
                ponto = abs(((tf - 5) * 0.2) - 10)
                pontoSom = ponto
            else:
                pontoSom = 10
        else:
            pontoSom = 0

        if (tasksub == sub):
            if (tf > 30):
                print('Tempo esgotado!')
            elif (tf > 5):
                ponto = abs(((tf - 5) * 0.2) - 10)
                pontoSub = ponto
            else:
                pontoSub = 10
        else:
            pontoSub = 0

        if (taskmult == mult):
            if (tf > 30):
                print('Tempo esgotado!')
            elif (tf > 5):
                ponto = abs(((tf - 5) * 0.2) - 10)
                pontoMult = ponto
            else:
                pontoMult = 10
        else:
            pontoMult = 0

        if (taskdiv == div):
            if (tf > 30):
                print('Tempo esgotado!')
            elif (tf > 5):
                ponto = abs(((tf - 5) * 0.2) - 10)
                pontoDiv = ponto
            else:
                pontoDiv = 10
        else:
            pontoDiv = 0

        pontoPlayer1 = int(pontoSom + pontoSub + pontoMult + pontoDiv)
        if (pontoPlayer1 > 0):
            print(f'Sua pontuação final foi {pontoPlayer1}. Tempo de Jogo:{tf:.2f}s')
        else:
            print('Errou tudo!')  # fim do esquema da pontuação

    else:
        print('INVALIDO')

    #PLAYER 2
    enter2 = input('(PLAYER 2)Aperte enter para começar')
    if (start == 1):
        t1 = time.time()

        n1 = random.randint(-10, 10)
        n2 = random.randint(-10, 10)
        som = n1 + n2
        tasksom = int(input(f'{n1} + {n2} ='))

        n1 = random.randint(-10, 10)
        n2 = random.randint(-10, 10)
        sub = n1 - n2
        tasksub = int(input(f'{n1} - {n2} ='))

        n1 = random.randint(-10, 10)
        n2 = random.randint(-10, 10)
        mult = n1 * n2
        taskmult = int(input(f'{n1} x {n2} ='))

        n1 = random.randint(-10, 10)
        n2 = random.randint(-10, 10)
        div = n1 // n2
        taskdiv = int(input(f'{n1} / {n2} ='))

        t2 = time.time()
        tf = t2 - t1

        # Esquema da pontuação
        if (tasksom == som):
            if (tf > 30):
                print('Tempo esgotado!')
            elif (tf > 5):
                ponto = abs(((tf - 5) * 0.2) - 10)
                pontoSom = ponto
            else:
                pontoSom = 10
        else:
            pontoSom = 0

        if (tasksub == sub):
            if (tf > 30):
                print('Tempo esgotado!')
            elif (tf > 5):
                ponto = abs(((tf - 5) * 0.2) - 10)
                pontoSub = ponto
            else:
                pontoSub = 10
        else:
            pontoSub = 0

        if (taskmult == mult):
            if (tf > 30):
                print('Tempo esgotado!')
            elif (tf > 5):
                ponto = abs(((tf - 5) * 0.2) - 10)
                pontoMult = ponto
            else:
                pontoMult = 10
        else:
            pontoMult = 0

        if (taskdiv == div):
            if (tf > 30):
                print('Tempo esgotado!')
            elif (tf > 5):
                ponto = abs(((tf - 5) * 0.2) - 10)
                pontoDiv = ponto
            else:
                pontoDiv = 10
        else:
            pontoDiv = 0

        pontoPlayer2 = int(pontoSom + pontoSub + pontoMult + pontoDiv)
        if (pontoPlayer2 > 0):
            print(f'Sua pontuação final foi {pontoPlayer2}. Tempo de Jogo:{tf:.2f}s')
        else:
            print('Errou tudo!')  # fim do esquema da pontuação

    elif (start == 2):
        t1 = time.time()

        n1 = random.randint(-100, 100)
        n2 = random.randint(-100, 100)
        som = n1 + n2
        tasksom = int(input(f'{n1} + {n2} ='))

        n1 = random.randint(-100, 100)
        n2 = random.randint(-100, 100)
        sub = n1 - n2
        tasksub = int(input(f'{n1} - {n2} ='))

        n1 = random.randint(-100, 100)
        n2 = random.randint(-100, 100)
        mult = n1 * n2
        taskmult = int(input(f'{n1} x {n2} ='))

        n1 = random.randint(-100, 100)
        n2 = random.randint(-100, 100)
        div = n1 // n2
        taskdiv = int(input(f'{n1} / {n2} ='))

        t2 = time.time()
        tf = t2 - t1

        # Esquema da pontuação
        if (tasksom == som):
            if (tf > 30):
                print('Tempo esgotado!')
            elif (tf > 5):
                ponto = abs(((tf - 5) * 0.2) - 10)
                pontoSom = ponto
            else:
                pontoSom = 10
        else:
            pontoSom = 0

        if (tasksub == sub):
            if (tf > 30):
                print('Tempo esgotado!')
            elif (tf > 5):
                ponto = abs(((tf - 5) * 0.2) - 10)
                pontoSub = ponto
            else:
                pontoSub = 10
        else:
            pontoSub = 0

        if (taskmult == mult):
            if (tf > 30):
                print('Tempo esgotado!')
            elif (tf > 5):
                ponto = abs(((tf - 5) * 0.2) - 10)
                pontoMult = ponto
            else:
                pontoMult = 10
        else:
            pontoMult = 0

        if (taskdiv == div):
            if (tf > 30):
                print('Tempo esgotado!')
            elif (tf > 5):
                ponto = abs(((tf - 5) * 0.2) - 10)
                pontoDiv = ponto
            else:
                pontoDiv = 10
        else:
            pontoDiv = 0

        pontoPlayer2 = int(pontoSom + pontoSub + pontoMult + pontoDiv)
        if (pontoPlayer2 > 0):
            print(f'Sua pontuação final foi {pontoPlayer2}. Tempo de Jogo:{tf:.2f}s')
        else:
            print('Errou tudo!')  # fim do esquema da pontuação

    elif (start == 3):
        t1 = time.time()

        n1 = random.randint(-1000, 1000)
        n2 = random.randint(-1000, 1000)
        som = n1 + n2
        tasksom = int(input(f'{n1} + {n2} ='))

        n1 = random.randint(-1000, 1000)
        n2 = random.randint(-1000, 1000)
        sub = n1 - n2
        tasksub = int(input(f'{n1} - {n2} ='))

        n1 = random.randint(-1000, 1000)
        n2 = random.randint(-1000, 1000)
        mult = n1 * n2
        taskmult = int(input(f'{n1} x {n2} ='))

        n1 = random.randint(-1000, 1000)
        n2 = random.randint(-1000, 1000)
        div = n1 // n2
        taskdiv = int(input(f'{n1} / {n2} ='))

        t2 = time.time()
        tf = t2 - t1

        # Esquema da pontuação
        if (tasksom == som):
            if (tf > 30):
                print('Tempo esgotado!')
            elif (tf > 5):
                ponto = abs(((tf - 5) * 0.2) - 10)
                pontoSom = ponto
            else:
                pontoSom = 10
        else:
            pontoSom = 0

        if (tasksub == sub):
            if (tf > 30):
                print('Tempo esgotado!')
            elif (tf > 5):
                ponto = abs(((tf - 5) * 0.2) - 10)
                pontoSub = ponto
            else:
                pontoSub = 10
        else:
            pontoSub = 0

        if (taskmult == mult):
            if (tf > 30):
                print('Tempo esgotado!')
            elif (tf > 5):
                ponto = abs(((tf - 5) * 0.2) - 10)
                pontoMult = ponto
            else:
                pontoMult = 10
        else:
            pontoMult = 0

        if (taskdiv == div):
            if (tf > 30):
                print('Tempo esgotado!')
            elif (tf > 5):
                ponto = abs(((tf - 5) * 0.2) - 10)
                pontoDiv = ponto
            else:
                pontoDiv = 10
        else:
            pontoDiv = 0

        pontoPlayer2 = int(pontoSom + pontoSub + pontoMult + pontoDiv)

        if (pontoPlayer2 > 0):
            print(f'Sua pontuação final foi {pontoPlayer2}. Tempo de Jogo:{tf:.2f}s')
        else:
            print('')
            print('Errou tudo!')  # fim do esquema da pontuação

    else:
        print('INVALIDO')

    if(pontoPlayer1 > pontoPlayer2):
        print('Player 1 Venceu!!')
        #placar
        print(f'Primeiro lugar - player 1 = {pontoPlayer1} pontos.')
        print(f'Segundo lugar - player 2 = {pontoPlayer2} pontos.')
    elif(pontoPlayer1 < pontoPlayer2):
        print('Player 2 Venceu!!')
        #placar
        print(f'Primeiro lugar - player 2 = {pontoPlayer2} pontos.')
        print(f'Segundo lugar - player 1 = {pontoPlayer1} pontos.')
    elif(pontoPlayer1 == pontoPlayer2):
        print('Empate')