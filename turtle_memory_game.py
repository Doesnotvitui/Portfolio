import random
from time import sleep
import turtle

# Função para criar a matriz de jogo


def criar_matriz(dificuldade):
    alphabetic = [
        "A", "B", "C", "D", "E", "F", "G", "H",
        "I", "J", "K", "L", "M", "N", "O", "P",
        "Q", "R", "S", "T", "U", "V", "W", "X",
        "Y", "Z", "1", "2", "3", "4", "5", "6",
        "7", "8", "9"
    ]

    mat_length = 4
    if dificuldade == "2":
        mat_length = 6
    elif dificuldade == "3":
        mat_length = 8

    letters = random.sample(alphabetic, mat_length * mat_length // 2) * 2
    random.shuffle(letters)

    mat = [letters[i * mat_length:(i + 1) * mat_length]
           for i in range(mat_length)]
    mat_exib = [['#' for _ in range(mat_length)] for _ in range(mat_length)]

    return mat, mat_exib

# Função para desenhar a matriz de jogo


def desenhar_matriz(mat_exib):
    turtle.clear()
    turtle.speed(0)
    turtle.hideturtle()
    tamanho = len(mat_exib)
    lado = 40

    for i in range(tamanho):
        for j in range(tamanho):
            x = j * lado - (tamanho * lado) / 2
            y = i * lado - (tamanho * lado) / 2
            desenhar_celula(x, y, mat_exib[i][j])

    atualizar_contadores()
    turtle.update()

# Função para desenhar uma célula da matriz


def desenhar_celula(x, y, simbolo):
    lado = 40
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(0)

    for _ in range(4):
        turtle.forward(lado)
        turtle.left(90)

    turtle.penup()
    turtle.goto(x + lado / 2, y + lado / 2 - 10)
    turtle.write(simbolo, align="center", font=("Arial", 16, "normal"))

# Função para atualizar os contadores de erros e acertos


def atualizar_contadores():
    turtle.penup()
    turtle.goto(-150, 200)
    turtle.pendown()
    turtle.write(f"Erros: {erros}", align="center",
                 font=("Arial", 16, "normal"))

    turtle.penup()
    turtle.goto(150, 200)
    turtle.pendown()
    turtle.write(f"Acertos: {acertos}", align="center",
                 font=("Arial", 16, "normal"))

# Função chamada quando o jogador clica em uma célula da matriz


def on_click(x, y):
    tamanho = len(mat_exib)
    lado = 40
    coluna = int((x + (tamanho * lado) / 2) // lado)
    linha = int((y + (tamanho * lado) / 2) // lado)

    if 0 <= linha < tamanho and 0 <= coluna < tamanho:
        revelar_posicao(linha, coluna)

# Função para revelar o símbolo de uma posição da matriz


def revelar_posicao(linha, coluna):
    global primeira_pos, segunda_pos, tentativas, mat_exib, mat, erros, acertos

    if mat_exib[linha][coluna] == '#':
        if not primeira_pos:
            primeira_pos = (linha, coluna)
            mat_exib[linha][coluna] = mat[linha][coluna]
        elif not segunda_pos:
            segunda_pos = (linha, coluna)
            mat_exib[linha][coluna] = mat[linha][coluna]

            desenhar_matriz(mat_exib)
            turtle.update()
            tentativas += 1
            sleep(1)

            if mat[primeira_pos[0]][primeira_pos[1]] != mat[segunda_pos[0]][segunda_pos[1]]:
                mat_exib[primeira_pos[0]][primeira_pos[1]] = '#'
                mat_exib[segunda_pos[0]][segunda_pos[1]] = '#'
                erros += 1
            else:
                acertos += 1

            primeira_pos = None
            segunda_pos = None

        desenhar_matriz(mat_exib)

        if all(mat_exib[i][j] == mat[i][j] for i in range(len(mat)) for j in range(len(mat[i]))):
            print(f"Parabéns! Você completou o jogo em {
                  tentativas} tentativas.")
            print(f"Erros: {erros}, Acertos: {acertos}")
            turtle.done()

# Função para desistir do jogo


def desistir(x, y):
    print("Você desistiu do jogo.")
    turtle.bye()

# Função para revelar todas as células do jogo por 5 segundos


def revelar_jogo(x, y):
    global mat_exib, revelacoes_restantes

    if revelacoes_restantes > 0:
        revelacoes_restantes -= 1
        celulas_nao_reveladas = [(i, j) for i in range(
            len(mat_exib)) for j in range(len(mat_exib[i])) if mat_exib[i][j] == '#']

        for i, j in celulas_nao_reveladas:
            mat_exib[i][j] = mat[i][j]

        desenhar_matriz(mat_exib)
        turtle.update()
        sleep(5)

        for i, j in celulas_nao_reveladas:
            mat_exib[i][j] = '#'

        desenhar_matriz(mat_exib)


# Função para criar um botão
def criar_botao(texto, x, y, funcao):
    botao = turtle.Turtle()
    botao.speed(0)
    botao.penup()
    botao.goto(x, y)
    botao.write(texto, align="center", font=("Arial", 16, "normal"))
    botao.goto(x, y - 20)
    botao.shape("square")
    botao.shapesize(stretch_wid=1.5, stretch_len=3)
    botao.fillcolor("lightgrey")
    botao.onclick(funcao)
    return botao

# Função para escolher a dificuldade do jogo


def escolher_dificuldade():
    tela = turtle.Screen()
    tela.title("Escolha a Dificuldade")
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(0, 100)
    turtle.write("Escolha a Dificuldade", align="center",
                 font=("Arial", 24, "normal"))
    turtle.goto(0, 50)
    turtle.write("1 - Fácil", align="center", font=("Arial", 18, "normal"))
    turtle.goto(0, 0)
    turtle.write("2 - Médio", align="center", font=("Arial", 18, "normal"))
    turtle.goto(0, -50)
    turtle.write("3 - Difícil", align="center", font=("Arial", 18, "normal"))

    dificuldade = turtle.textinput(
        "Dificuldade", "Escolha a dificuldade (1, 2, 3):")
    tela.clear()
    return dificuldade

# Função principal do jogo


def jogo_da_memoria():
    global mat, mat_exib, primeira_pos, segunda_pos, tentativas, erros, acertos, revelacoes_restantes

    # Escolha da dificuldade
    dificuldade = escolher_dificuldade()
    if dificuldade not in ["1", "2", "3"]:
        print("Dificuldade inválida!")
        return

    # Inicialização das variáveis do jogo
    mat, mat_exib = criar_matriz(dificuldade)
    primeira_pos = None
    segunda_pos = None
    tentativas = 0
    erros = 0
    acertos = 0
    revelacoes_restantes = 2

    # Configurações da tela do Turtle
    turtle.tracer(0, 0)
    desenhar_matriz(mat_exib)

    # Criação dos botões
    criar_botao("Revelar", -100, -200, revelar_jogo)
    criar_botao("Desistir", 100, -200, desistir)

    # Eventos do Turtle
    turtle.onscreenclick(on_click)
    turtle.done()


# Chamada da função principal
if __name__ == "__main__":
    jogo_da_memoria()
