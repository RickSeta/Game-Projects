from cartas import *
from interacao import *


#feito por Henrique Yan de Seta Coutinho
janela = Window(1200,750)
janela.set_title("Jogo da Memoria")

fundo = Sprite("fundo.png")
fundo.x = -30
fundo.y = 0

tecla = Window.get_keyboard()

fundoCarta = Sprite("fundoCarta.png")

listaCartas, fundosCartas, listaSolucao = geraQuadros()

tabelaPermissaoFundos = criaLista(5,4,1)
tabelaPermissaoCartas = criaLista(2,10,2)

atualiza = True

deltaClique, segurando, cordX, cordY = 0,False,0,0
while True:

    deltatime = janela.delta_time()
    deltaClique += deltatime
    deltaClique ,segurando, cordX, cordY, atualiza= checaclique(fundosCartas, deltaClique, tabelaPermissaoFundos, tabelaPermissaoCartas, listaSolucao, segurando, cordX, cordY, atualiza)


    fundo.draw()
    desenhaCartas(listaCartas, tabelaPermissaoCartas)
    desenhaCartas(fundosCartas, tabelaPermissaoFundos)
    janela.update()

    if checaSolucao(tabelaPermissaoFundos):
        break

while True:
    fundoFinal = Sprite("fundoFinal.png")
    fundoFinal.draw()
    janela.update()
#feito por Henrique Yan de Seta Coutinho

