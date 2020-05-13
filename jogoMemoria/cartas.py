import random

from PPlay.sprite import *
#feito por Henrique Yan de Seta Coutinho


def criaLista(nLin,nColuna, modo = 0):
    # feito por Henrique Yan de Seta Coutinho
    lista = []
    if modo == 1:
        for x in range(nLin):
            linha = []
            for y in range(nColuna):
                linha.append(True)
            lista.append(linha)
        return lista
    if modo == 0:
        for x in range(nLin):
            linha = []
            for y in range(nColuna):
                linha.append(0)
            lista.append(linha)
        return lista

    for x in range(nLin):
        linha = []
        for y in range(nColuna):
            linha.append(False)
        lista.append(linha)
    return lista

def geraQuadros():
    mpPosX, mpPosY = 0 , 0
    cont =0
    fundosCartas = geraFundosCarta()
    vetNomes = ["abelha", "avestruz", "baleia", "cachorro", "cavalo", "coruja", "gato", "jacare", "tubarao", "urso"]
    vet1 = criaLista(2,10)
    listaSolucao = criaLista(2,10)
    for x in range(1):
        for y in range(10):
            num = random.randint(0,len(vetNomes)-1)

            vet1[x][y] = Sprite(str(vetNomes[num] + ".png"))
            vet1[x][y].x = 205 * mpPosX + 10 * mpPosX + 50
            vet1[x][y].y = 184 * mpPosY + 10 * mpPosY

            print(cont)
            listaSolucao[x][y] = cont
            listaSolucao[1-x][9-y] = cont
            cont += 1
            vet1[1-x][9-y] = Sprite(str(vetNomes[num] + "OK.png"))
            vet1[1][9 - y].x = 890 - 205 * mpPosX + 10
            vet1[1][9 - y].y = 566 - 184 * mpPosY + 10 * mpPosY
            #print(mpPosX,mpPosY)
            mpPosX += 1
            if mpPosX == 5:
                mpPosX = 0
                mpPosY += 1

            if mpPosY == 4:
                mpPosY = 0

            vetNomes.pop(num)

    return vet1, fundosCartas, listaSolucao
#feito por Henrique Yan de Seta Coutinho
def desenhaCartas(vetor, tabelaPermissao):
    for x in range(len(vetor)):
        for y in range(len(vetor[x])):
            if tabelaPermissao[x][y]:
                vetor[x][y].draw()


def geraFundosCarta():
    listaFundos = criaLista(5,4)
    for x in range(5):
        for y in range(4):
            listaFundos[x][y] = Sprite("fundoCarta.png")

            listaFundos[x][y].x = 205 * x + 10 * x + 50
            listaFundos[x][y].y = 184 * y+ 10 * y

    # feito por Henrique Yan de Seta Coutinho
    return listaFundos

