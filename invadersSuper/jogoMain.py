
from random import randint
from PPlay.window import *
from tiros import *
from inimigos import *
from PPlay.collision import *
from PPlay.gameimage import *



janela = Window(1200,501)
fundoMenu = GameImage("fundoMenu.jpg")



botao1 = Sprite("botaoJogar.png")
botao1.x = janela.width/2
botao1.y = janela.height/2

facilBut = Sprite("facilBut.png")

medioBut = Sprite("medioBut.png")
medioBut.x = janela.width - medioBut.width

dificilBut = Sprite("dificilBut.png")
dificilBut.x = janela.width /2
dificilBut.y = janela.height - dificilBut.height


difMenuBut = Sprite("difMenuBut.png")

mouse = Window.get_mouse()

state = 0

while True:

    fundoMenu.draw()

    if state == 0: #menu principal
        botao1.draw()
        difMenuBut.draw()

        if(mouse.is_over_object(botao1)):
            if(mouse.is_button_pressed(1)):
                state = 4
        if (mouse.is_over_object(difMenuBut)):
            if (mouse.is_button_pressed(1)):
                state = 1

    if state == 1:           #menu dificuldade
        facilBut.draw()
        medioBut.draw()
        dificilBut.draw()

        if(mouse.is_over_object(facilBut)):
            if (mouse.is_button_pressed(1)):
                dificuldade =1
                break

        if(mouse.is_over_object(medioBut)):
            if (mouse.is_button_pressed(1)):
                dificuldade = 2
                break

        if (mouse.is_over_object(dificilBut)):
            if (mouse.is_button_pressed(1)):
                dificuldade = 3
                break

    janela.update()
    if state == 4:
        dificuldade = 1
        break

# -------------------------------------fim menu---------------------------




# -------------------------------definição variaveis----------------------
janela = Window(1300, 700)  # janela e tamanho

nave = Sprite("nave.png")  # sprite da nave

nave.y = janela.height - nave.height
nave.x = janela.width / 2

velTiro = 500

listaTirosNave = []


listaInimigo, listaVida, velInimigo, limiteTiro, vidaNave, velNave = criaInimigo(dificuldade)

deltaSpace = 0  # contador de tempo para tiros do player
deltaSpoice = 0  # contador de tempo para tiros do inimigo
tecla = Window.get_keyboard()

vira = 1

listaTirosInimigos = []

tiraTiro = []  # contem as posições a serem retiradas na lista de tiros da nave

contaFrames, secCounter, previous = 0, 0, 0

mortos = 0

lose = False
win = False

deltaSuper = 0
listaSuperTiro = []

cronometro, score = 0,0
# ---------------------------------------loop principal -------------------------------------------
while True:


    deltatime = janela.delta_time()
    cronometro += deltatime
    contaFrames += 1

    vira = moveInimigo(vira, janela, deltatime, listaInimigo, velInimigo)
    if nave.x >= 0 and nave.x <= janela.width - nave.width:  # se a nave estiver na tela
        nave.move_key_x(velNave * deltatime)    # pode se mover de acordo com a velocidade e o tempo entre os game loops

    elif nave.x < 0:  # se ultrapassar a tela coloca de volta na mesma hora
        nave.x += 1
    else:
        nave.x -= 1

# ---------------------relacionado a tiro da nave-----------------
    deltaSpace += deltatime  # soma o tempo a cada loop para possibilitar contabilizar o tiro ou nao

    if deltaSpace > limiteTiro:  # se o tempo para o proximo tiro for suficiente pode checar se espaço esta pressionado
        if tecla.key_pressed("SPACE"):
            if(deltaSuper >= 2):
                print("Entrou aquii")
                superTiro = True
                criaTiro(nave, listaSuperTiro, "superTiro.png")
                deltaSpace = 0
                deltaSuper = 0
            else:
                superTiro = False

            if(superTiro == False and deltaSuper == 0 ):
                criaTiro(nave, listaTirosNave, "tiro.png")
                deltaSpace = 0  # reseta o cooldown para que nao haja tiros sucessivos

            deltaSuper += deltatime
            print("Aumentou o super")
        else:
            print("Zerou super")
            deltaSuper = 0

    passaTiros(velTiro, deltatime, listaTirosNave)
    removeTiro(0, listaTirosNave)

    passaTiros(velTiro, deltatime, listaSuperTiro)
    removeTiro(0,listaSuperTiro)
# -----------------------------------------------------------------


# ----------------------relacionado a tiros do inimigo-------------
    deltaSpoice += deltatime

    if(deltaSpoice > 0.7):
        tiroInimigo(listaInimigo, listaTirosInimigos, dificuldade)
        deltaSpoice = 0
    passaTiros(velTiro, deltatime, listaTirosInimigos,1)
    removeTiro(2,listaTirosInimigos, alturaJanela=janela.height)

# -----------------------------------------------------------------



# ---------------------colisoes tiro no inimigo-------------------
    for x in range(len(listaTirosNave)):
        for i in range(len(listaInimigo)):
            for j in range(len(listaInimigo[0])):

                if(listaInimigo[i][j]) != None :
                    if (Collision.collided_perfect(listaTirosNave[x], listaInimigo[i][j])):
                        listaVida[i][j] -= 1
                        tiraTiro.append(x)
                        if(listaVida[i][j] <= 0):
                            listaInimigo[i][j] = None
                            score += 1000 * dificuldade * 1/cronometro
                            mortos += 1
                            velInimigo *= 1.1
                            if dificuldade == 3:
                                velInimigo *= 1.1

    for x in range(len(tiraTiro)-1, 0, -1):
        removeTiro(1, listaTirosNave, tiraTiro[x])
        tiraTiro.pop(x)

    for x in range(len(listaSuperTiro)):    # checa colisao do super tiro
        for i in range(len(listaInimigo)):
            for j in range(len(listaInimigo[0])):
                if (listaInimigo[i][j]) != None:
                    if (Collision.collided_perfect(listaSuperTiro[x], listaInimigo[i][j])):
                        listaInimigo[i][j] = None
                        score += 1000 * dificuldade * 1 / cronometro
                        mortos += 1
                        velInimigo *= 1.1
                        if dificuldade == 3:
                            velInimigo *= 1.1

    for x in range(len(listaTirosInimigos)):
        if (Collision.collided_perfect(listaTirosInimigos[x], nave)):
            vidaNave -= 1
            tiraTiro.append(x)
            if(vidaNave <= 0):
                print("PerdeU!!!")

    for x in range(len(tiraTiro)-1, 0, -1):
        removeTiro(1, listaTirosInimigos, tiraTiro[x])
        tiraTiro.pop(x)
# ------------------------------------------------------------
    janela.set_background_color((0, 0, 0))

    secCounter += deltatime
    if(secCounter >= 1):
        contaFrames = (contaFrames/deltatime)/100
        previous = contaFrames
        Window.draw_text(janela,text=str(contaFrames),x=0,y=0,color=(255,255,255),size=20)

        contaFrames ,secCounter = 0,0
    else:
        Window.draw_text(janela, text=str(previous), x=0, y=0, color=(255, 255, 255),size=20)


    drawTiros(listaTirosNave)

    drawTiros(listaTirosInimigos)
    drawTiros(listaSuperTiro)

    if mortos == len(listaInimigo) * len(listaInimigo[0]):
        listaTirosInimigos, listaTirosNave = [], []

        dificuldade += 1
        if(dificuldade == 4):
            win = True
            break

        listaInimigo, listaVida, velInimigo, limiteTiro, vidaNave, velNave = criaInimigo(dificuldade)


        mortos = 0

    lose = drawInimigo(listaInimigo, vidaNave,nave)
    if lose:
        del listaTirosNave
        del listaTirosInimigos
        del listaInimigo
        break



    nave.draw()
    janela.update()


Window.draw_text(janela, text="Digite seu nome", x=150, y=janela.height / 2 - 200, color=(255, 165, 0),
                 size=150, font_name="stencil")
janela.update()
nome = input("nome: ")

arq = open('pontos.txt', "r")
conteudo = arq.readlines()
conteudo.append('\nNome: ' + nome + " Pontuacao: " + str(score))
listita = conteudo
arq = open("pontos.txt", 'w')
arq.writelines(conteudo)
arq.close()


for k in range(len(listita)):

    print(listita[k])



while True:
    r,g,b = randint(0,255), randint(0,255), randint(0,255)
    janela.set_background_color((0, 0, 0))

    if lose:
        Window.draw_text(janela, text="Game over", x=200, y=janela.height / 2 -200, color=(255,165,0),
                     size=200, font_name="stencil")
    if win:
        Window.draw_text(janela, text="VENCEDOR", x=200, y=janela.height / 2 - 200, color=(r, g, b),
                         size=200, font_name="stencil")

    for k in range(len(listita)):
        char = listita[k]
        Window.draw_text(janela, text=char, x=100, y=janela.height / 2 + 300 + 20 * k, color=(255, 165, 255), size=20,
                         font_name="stencil")

    janela.update()

