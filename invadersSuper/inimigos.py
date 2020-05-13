from PPlay.sprite import *

from PPlay.collision import *


def criaLista(nLin,nColuna):

    lista = []

    for x in range(nLin):
        linha = []
        for y in range(nColuna):
            linha.append(0)
        lista.append(linha)
    return lista


def criaInimigo(dificuldades):

    if dificuldades == 1:
        nLin = 2
        nColuna = 7
        tomaTiro = 3
        velInimigo = 200
        limiteTiro = 1
        vidaNave = 3
        velNave = 500 / dificuldades

    elif(dificuldades == 2):
        nLin = 4
        nColuna = 7
        tomaTiro = 3
        velInimigo = 110
        limiteTiro = 0.6
        vidaNave = 3
        velNave = 500 / dificuldades
    else:
        nLin = 3
        nColuna = 3
        tomaTiro = 10
        velInimigo = 100
        limiteTiro = 1
        vidaNave = 3
        velNave = 500

    listaInimigo = criaLista(nLin,nColuna)
    listaVida = criaLista(nLin,nColuna)

    for i in range(nLin):
        for j in range(nColuna):  #aqui faz o mesmo que antes porem variando as coordenadas a partir do primeiro
            listaVida[i][j] = tomaTiro
            if i == 0 and j == 0:
                if(dificuldades == 1):
                    listaInimigo[0][0] = Sprite("inimigoEasy.png")  # cria o primeiro inimigo sendo o sprite em questao e a sua quantidade de tiros que pode tomar
                if(dificuldades == 2):
                    listaInimigo[0][0] = Sprite("inimigoMedio.png")
                if(dificuldades == 3):
                    listaInimigo[i][j] = Sprite("boss.png")

                listaInimigo[0][0].x = 0
                listaInimigo[0][0].y = -1 * listaInimigo[0][0].height * (nLin / 2)
            else:
                if(dificuldades == 1):
                    listaInimigo[i][j] = Sprite("inimigoEasy.png")
                elif(dificuldades == 2):
                    listaInimigo[i][j] = Sprite("inimigoMedio.png")
                elif(dificuldades == 3):
                    listaInimigo[i][j] = Sprite("boss.png")


                listaInimigo[i][j].x =  (listaInimigo[0][0].width * j) + 50 * j

                listaInimigo[i][j].y = listaInimigo[0][0].y + (listaInimigo[0][0].height * i) + 1 * i

    return listaInimigo, listaVida, velInimigo, limiteTiro, vidaNave, velNave

def moveInimigo( vira,janela, contadorTempo, listaInimigo, velInimigo): # nome da janela, e lista de inimigos

    if(contadorTempo > 2):
        return vira

    movY = False
    notDone = True
    for x in range(len(listaInimigo)):
        if notDone:
            for y in range(len(listaInimigo[0])):

                if (listaInimigo[x][y] != None and listaInimigo[x][y].x < 0):
                    vira = 1
                    movY = True
                    notDone = False
                    break

                elif (listaInimigo[x][-y] != None):
                    if (listaInimigo[x][-y].x >= janela.width - listaInimigo[x][-y].width):

                        movY = True
                        vira = -1
                        notDone = False
                        break
        else:
            break

    for x in range(len(listaInimigo)):
        for y in range(len(listaInimigo[0])):

            if listaInimigo[x][y] != None:
                listaInimigo[x][y].x += velInimigo * contadorTempo * vira
                if(movY):
                    if(vira > 0):
                        listaInimigo[x][y].x += 10
                    else:
                        listaInimigo[x][y].x -= 10
                    listaInimigo[x][y].y += 10
    return vira

def drawInimigo(listaInimigo,vidaNave,nave):

    for i in range(len(listaInimigo)):  #desenha todos inimigos
        for j in range(len(listaInimigo[0])):
            if listaInimigo[i][j] != None:
                listaInimigo[i][j].draw()
                if (Collision.collided(listaInimigo[i][j], nave) or vidaNave <= 0):
                    return True
    return False


def removeInimigo(listaInimigo,listaVida):

    for y in range (len(listaInimigo)):
        for z in range (len(listaInimigo[0])):
            if listaVida[y][z] <= 0:
                listaInimigo[y][z] = None