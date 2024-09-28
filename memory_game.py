import os
import random
from time import sleep


def criar_matriz(dificuldade):
    # aqui é criada as matrizes de acordo com a dificuldade

    mat = []
    mat_exib = []

    alphabetic = [
        "A", "B", "C", "D",
        "E", "F", "G", "H",
        "I", "J", "K", "L",
        "M", "N", "O", "P",
        "Q", "R", "S", "T",
        "U", "V", "W", "X",
        "Y", "Z", "1", "2",
        "3", "4", "5", "6",
        "7", "8", "9"
    ]

    mat_length = 4

    if dificuldade == "2":
        mat_length = 6
    elif dificuldade == "3":
        mat_length = 8

    letters = []

    # aqui é criado as letras que vão ser usadas na matriz
    for _ in range((mat_length * mat_length) // 2):

        # print(alphabetic)
        index = random.randint(0, len(alphabetic) - 1)
        letter = alphabetic.pop(index)

        letters.append(letter)

    # aqui é criado a matriz
    letters_hash = {letter: 0 for letter in letters}

    for i in range(mat_length):
        col = []

        for j in range(mat_length):
            index = random.randint(0, len(letters) - 1)
            letter = letters[index]

            letters_hash[letter] += 1

            if letters_hash[letter] == 2:
                letters.pop(index)

            col.append(letter)

        mat.append(col)
        mat_exib.append(["#" for _ in range(len(col))])

    return mat, mat_exib


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def atualiza(pos1, pos2, mat, mat_exib):
    # verifica se os pares de símbolos conferem
    # e atualiza matriz
    # obs: pode-se considerar pos1,pos2 uma tupla [linha,coluna]
    # exemplo:
    # pos1=[0,0] ou seja, x=0,y =0
    # pos2=[3,5] ou seja, x=3,y =5

    x1, y1 = int(pos1[0]), int(pos1[1])
    x2, y2 = int(pos2[0]), int(pos2[1])

    if mat[x1][y1] == mat[x2][y2]:
        mat_exib[x1][y1] = mat[x1][y1]
        mat_exib[x2][y2] = mat[x2][y2]
    else:
        limpar_tela()
        print("Os pares não conferem!")
        print()

        mat_exib[x1][y1] = mat[x1][y1]
        mat_exib[x2][y2] = mat[x2][y2]

        exibir_mat(mat_exib)
        sleep(2)

        mat_exib[x1][y1] = "#"
        mat_exib[x2][y2] = "#"

    return mat, mat_exib


def exibir_mat_exib(mat_exib):
    # exibe a matriz de exibição
    # obs: a matriz de exibição é a matriz que o jogador vê
    # a matriz resposta é a matriz que o jogador não vê
    # aqui é criado a matriz de exibição

    exibir_mat(mat_exib)


def exibir_mat(mat):
    print("   " + "   ".join([str(i) for i in range(len(mat[0]))]))
    index = 0

    for row in mat:
        row_exib = f"{index}  "

        col_index = 0

        for col in row:
            if col_index != 0:
                row_exib += f" | "

            row_exib += f"{col}"
            col_index += 1

        print(row_exib)
        index += 1


def exibir_resp(mat):
    # exibe a matriz resposta por 3 segundos
    # no maximo 2x

    exibir_mat(mat)
    sleep(3)


while True:
    limpar_tela()

    print("JOGO DA MEMÓRIA")
    print()

    print("Escolha a dificuldade:")
    print("1 - Fácil")
    print("2 - Médio")
    print("3 - Difícil")

    dificuldade = input()

    if dificuldade != "1" and dificuldade != "2" and dificuldade != "3":
        print("Dificuldade inválida!")
        continue

    show_answers_count = 2
    mat, mat_exib = criar_matriz(dificuldade)

    while True:
        limpar_tela()
        exibir_mat_exib(mat_exib)

        print()

        print("1 - Jogar")
        print(f"2 - Exibir respostas (Vezes restantes: {show_answers_count})")
        print("3 - Sair")

        option = input()

        if option == "1":
            pos1 = input("Escolha a primeira posição: ")
            pos2 = input("Escolha a segunda posição: ")

            mat, mat_exib = atualiza(pos1, pos2, mat, mat_exib)

            if mat_exib == mat:
                exibir_mat_exib(mat_exib)
                print()
                print("Você ganhou!")
                break
        elif option == "2":
            if show_answers_count == 0:
                print("Você não pode mais exibir as respostas!")
                continue

            limpar_tela()
            exibir_resp(mat)
            show_answers_count -= 1
        elif option == "3":
            print("Você saiu do jogo!")
            break

    print()
    print("1 - Jogar novamente")
    print("2 - Sair")

    option = input()

    if option == "2":
        break

print()
print("Obrigado por jogar!")
