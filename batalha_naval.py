# -*- coding utf-8 -*-
import random
def kant(tab):
    for i in tab:
        for j in range(len(i)):
            if i[j] == '~':
                i[j] = '~'
        print(" ".join(i))
       

tab1 = []
tab2 = []
for i in range(18):
    tab1.append(['~']*18)
    tab2.append(["~"]*18)        

def leonboff(tab2, boats):
    one_direction=['V','H']
    l=[]
    for i in boats:
        while True:
            line=random.randint(1,17)
            column=random.randint(1,17)
            l.append(line)
            l.append(column)
            try:
                while line in l or column in l:
                    line=line=random.randint(1,17)
                    column=random.randint(1,17)
                x=cortella(random.choice(one_direction), line, column, i, tab2, pinto_pequeno)
                while x == False:
                    x=cortella(random.choice(one_direction), line, column, i, tab2, pinto_pequeno)
                    line=random.randint(1,17)
                    column=random.randint(1,17)
            except:
                pass
            else:
                break
        
def berkeley(tab1):
    line=random.randint(0,17)
    column=random.randint(0,17)
    x=bauman(line, column, tab1)
    
        

            
porta_aviao =  5 
encouracado = 4
submarino = 3
destroyer = 3
barco = 2
boats=[porta_aviao, encouracado, submarino, destroyer,barco]
titulo=['Porta Aviões', 'Encouraçado', 'Submarino', 'Destroyer', 'Barco']
vai_pra_cuba = 'R'
pinto_pequeno =  'O'


def Niet(direcao, l, c, tipo, tab, carac):
    if tab[l][c] != 0:
        print("TEM BARCO CARALHO!!")
        





def cortella (direcao, l, c,tipo,tab, carac):

    lista=[]
    x=0
    if direcao == 'H':
        for i in range(tipo):
            lista.append(tab[l][c+i])
            for j in lista:
                if j!='~':
                    x+=1
            
        if x==0:        
            tab[l][c]=carac
            for i in range(tipo):
                tab[l][c+i]=carac
                    

        else:
            while tab1[l][c] == "R": 
                print("TEM BARCO CARALHO!!")
                l= int(input("Digite uma linha válida:"))
                c= int(input("Digite uma coluna válida:"))
            tab[l][c]=carac
            for i in range(tipo):
                tab[l][c+i]=carac

    elif direcao == 'V':
        for i in range(tipo):
            lista.append(tab[l+i][c])
            for j in lista:
                if j!='~':
                    x+=1
        if x==0:        
            tab[l][c]=carac        
            for i in range(tipo):
                tab[l+i][c]=carac
        else:
            while tab1[l][c] == "R": 
                print("TEM BARCO CARALHO!!")
                l= int(input("Digite uma linha válida:"))
                c= int(input("Digite uma coluna válida:"))
            tab[l][c]=carac
            for i in range(tipo):
                tab[l+1][c]=carac

#cortella('H', 3,3, porta_aviao, tab1, vai_pra_cuba)

def bauman(linha, coluna, tabu):
    if tabu[linha][coluna]=='~':
        tabu[linha][coluna] ='X'
        if tabu==tab2:
            print("Sorry, you miss the boat")
        return False
    elif tabu[linha][coluna]==pinto_pequeno or tabu[linha][coluna]==vai_pra_cuba:
        tabu[linha][coluna] = "*"
        if tabu==tab2:
            print("Congratulations, you beat it")
        return True

print("POSICIONAMENTO DOS BARCOS")
for i in boats:
    print('Posicione o barco %s de tamanho %dx1'%(titulo[boats.index(i)], i))
    pitagoras =  input("Em qual direção vc deseja jogar[V/H]:").upper()
    parmenides = int(input ("Qual a linha que vc desenha jogar:"))
    platao = int(input ("Qual a coluna que vc deseja jogar:"))
    cortella(pitagoras, parmenides, platao, i,tab1, vai_pra_cuba)
leonboff(tab2, boats)
