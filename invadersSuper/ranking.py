from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *


def ranking(janela,mouse):

  logo = Sprite("img/logo.png")

  back = Sprite("img/dific/back1.png")
  play1 = Sprite("img/dific/play1.png")

  back2 = Sprite("img/dific/back2.png")
  play2 = Sprite("img/dific/play2.png")

  back.set_position(janela.width / 2 - back.width - 40, 650)
  play1.set_position(janela.width / 2 + 40, 650)
  logo.set_position(janela.width / 2 - logo.width / 2, 100)
  back2.set_position(janela.width / 2 - back.width - 40, 650)
  play2.set_position(janela.width / 2 + 40, 650)


  arq = open('ranking.txt','r')  # abre o arquivo
  conteudo = arq.readlines() #transforma o arquivo em array
  print(conteudo)
  nomes=[] #fiz essas 2 pra separar nome do que é ponto
  pontos=[]
  for i in range(len(conteudo)):
    linha=conteudo[i].split() # a informação vem assim "(nome) (dific) (pontos)"
    nomes.append(linha[0]) # aqui eu coloquei todos os nomes numa lista
    pontos.append(int(linha[2].rstrip('\n'))) # aqui coloquei todos os pontos
  arq.close()
  for j in range(5): # aqui é pra ordenar do maior pro menor
    for i in range(len(pontos)-1):
      if pontos[i]<pontos[i+1]: #se a pontuaçao for menor, troca os pontos e o nome nas listas
        pontos[i+1],pontos[i]=pontos[i],pontos[i+1]
        nomes[i+1],nomes[i]=nomes[i],nomes[i+1]

  while True:
    janela.set_background_color((0, 0, 0))
    logo.draw()

    for i in range(len(nomes)):
      if i>4:
        break
      janela.draw_text("{}".format(nomes[i]), 180, 280+i*40, size=20, color=(255, 255, 255))
      janela.draw_text("{}".format(pontos[i]), 400, 280+i*40, size=20, color=(255, 255, 255))

    if mouse.is_over_object(back):
      back2.draw()
      if mouse.is_button_pressed(1):
        return 1
    else:
      back.draw()
    if mouse.is_over_object(play1):
      play2.draw()
      if mouse.is_button_pressed(1):
        return 4
    else:
      play1.draw()
    janela.update()
