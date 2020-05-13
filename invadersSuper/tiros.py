from PPlay.sprite import *
from PPlay.collision import *
from random import randint

def criaTiro(atirador, arrayTiros, SpriteNome, tipo = 0):
    tiro = Sprite(SpriteNome)   #cria um novo tiro/sprite
    if tipo == 0:
        tiro.x = atirador.x + atirador.width/2 - tiro.width/2  #posiciona onde a nave se econtra naquele momento
        tiro.y = atirador.y - atirador.height/2
    elif tipo == 1:
        tiro.x = atirador.x + atirador.width / 2 - tiro.width / 2  # posiciona onde a nave se econtra naquele momento
        tiro.y = atirador.y + atirador.height / 2 + 3

    arrayTiros.append(tiro) #adiciona o tiro na lista

def passaTiros(velocidade,contadorTempo, arrayTiros,tipo = 0):

    if tipo == 0:
        sentido = 1
    else:
        sentido = -1

    for x in range(len(arrayTiros)):    #passa por todos tiros existentes na lista
        arrayTiros[x].y -= velocidade * contadorTempo * sentido  #faz os tiros subirem com base na velocidade



def removeTiro(tipo,arrayTiros,numTiro = 0,alturaJanela = 0):
    """Remove tiros com base em consequencia, tipo 0 é sair da tela , 1 é atingir nave/inimigo, 2 é tiro inimigo passar da tela
        recebe um int tipo e uma lista arrayTiros"""

    if tipo == 0:
        if len(arrayTiros) > 0:
            if arrayTiros[0].y <= -1 * arrayTiros[0].height:  # se um tiro estiver completamente fora da tela
                arrayTiros.pop(0) #destrua-o

    elif tipo == 1:
        arrayTiros.pop(numTiro)

    elif tipo == 2:
        if len(arrayTiros) > 0:
            if arrayTiros[0].y > alturaJanela:  # se um tiro estiver completamente fora da tela
                arrayTiros.pop(0) #destrua-o

def tiroInimigo(listaInimigo, listaTirosInimigos,dificuldade):

    for i in range(len(listaInimigo)):
        for j in range(len(listaInimigo[0])):
            if dificuldade == 1:
                chance = 10 + randint(1, 60)
            elif dificuldade == 2:
                chance = 40/(len(listaInimigo)) + randint(1,60)
            elif dificuldade == 3:
                chance = randint(20,80) + 30/(len(listaInimigo))

            if(chance > 60 and listaInimigo[i][j] != None):
                criaTiro(listaInimigo[i][j],listaTirosInimigos,"tiro.png")
                if dificuldade == 3:
                    criaTiro(listaInimigo[i][j], listaTirosInimigos, "tiro.png",1)

def drawTiros(listaTiros):
    for x in range(len(listaTiros)): #desenha todos os tiros
        listaTiros[x].draw()
