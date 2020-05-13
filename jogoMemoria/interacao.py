from time import sleep
from PPlay.window import *
#feito por Henrique Yan de Seta Coutinho
def checaclique(listaFundos,deltaClique,tabelaPermissaoFundos,tabelaPermissaoCartas, listaSolucao,segurando, cordX, cordY,atualiza):
    mouse = Window.get_mouse()
    for x in range(5):
        for y in range(4):
            if (mouse.is_over_object(listaFundos[x][y])):
                if (mouse.is_button_pressed(1) and deltaClique > 0.5) or not atualiza:
                    #print("CLICK")
                    deltaClique = 0

                    if not segurando:
                        cordX, cordY = x, y
                        tabelaPermissaoFundos[x][y] = False
                        newX, newY = conversor(x, y)
                        tabelaPermissaoCartas[newX][newY] = True
                        segurando = True
                    else:
                        if atualiza:
                            atualiza = False
                            tabelaPermissaoFundos[x][y] = False
                            newX, newY = conversor(x, y)
                            tabelaPermissaoCartas[newX][newY] = True
                            break
                        else:
                            atualiza = True
                        #print("Checando compativel")
                        if checaCompativel(listaSolucao, cordX,cordY, x, y):
                            sleep(2)
                            newX, newY = conversor(cordX, cordY)
                            tabelaPermissaoFundos[cordX][cordY], tabelaPermissaoCartas[newX][newY] = False, False
                            newX, newY = conversor(x, y)
                            #print(x,y, newX,newY)
                            tabelaPermissaoFundos[x][y], tabelaPermissaoCartas[newX][newY] = False, False

                        else:
                            sleep(2)
                            tabelaPermissaoFundos[cordX][cordY] = True
                            tabelaPermissaoFundos[x][y] = True
                            newX, newY = conversor(cordX, cordY)
                            tabelaPermissaoCartas[newX][newY] = False
                            newX, newY = conversor(x, y)
                            tabelaPermissaoCartas[newX][newY] = False
                        segurando = False
    return deltaClique, segurando, cordX, cordY, atualiza


#feito por Henrique Yan de Seta Coutinho
def checaCompativel( listaSolucao, cordX, cordY, x, y):
    #print(x, y)

    x1,y1 = conversor(x,y)
    x2,y2 = conversor(cordX,cordY)

    #print(x1,y1,x2,y2)

    if listaSolucao[x1][y1] == listaSolucao[x2][y2]:
        return True
    else:
        return False

def conversor(y,x):
    saidaY = y
    if (x == 1 or x == 3):
        saidaY = 5 + y
    if x == 1:
        return 0 ,saidaY
    if x == 2:
        return 1, saidaY
    if x == 3:
        return 1 ,saidaY
    # feito por Henrique Yan de Seta Coutinho
    return x,y

def checaSolucao(lista):
    for linha in lista:
        for coluna in linha:
            if coluna:
                return False
    # feito por Henrique Yan de Seta Coutinho
    sleep(2)
    return True
