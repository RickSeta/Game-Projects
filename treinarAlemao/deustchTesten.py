import random
vet = ["Auge ", "Nase ", "Mund ", "Kopf ", "Ohr ", "Busen ", "Rücken ", "Brust ", "Fuß ", "Bauch ", "Bein ", "Arm ", "Hals ", "Schulter ", "Finger ", "Haar ", "Knie ", "Hand "]
tipos = [2,3,1,1,2,1,1,3,1,1,2,1,1,3,1,2,2,3]
#der 1, das 2, die 3
 
fim = 0
descart = []

def jaFoi(nume):

    if nume not in descart:
        descart.append(nume)
        #input(nume)
    else:
        nume = random.randint(0,len(vet)-1)
        nume = jaFoi(nume)
    return nume
    
def pergunta(num):
    
    
    print("1-Der 2-Das 3-Die \n")
    if int(input("Qual artigo de " + vet[num])) == tipos[num]:
        print("Acertou!!! \n")
    else:
        
        temp = ["Der", "Das", "Die"]
        print("Errou!!! Era " + temp[tipos[num]-1] + " \n")

    input()
    

while(fim <= len(vet)-1):
      
      num = random.randint(0,len(vet)-1)
      num = jaFoi(num)

      pergunta(num)
      
      fim += 1
              
