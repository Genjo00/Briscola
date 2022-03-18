from time import sleep

from random import randint

print('\n'*10)
print("        ######  ######   ######   ######   ######   #####   #          #\n        #     # #     #    #     #        #        #     #  #         # #\n        #     # #     #    #     #        #        #     #  #        #   # \n        ######  ######     #      #####   #        #     #  #       #     #\n        #     # #   #      #           #  #        #     #  #       #######\n        #     # #    #     #           #  #        #     #  #       #     #\n        ######  #     #  #####   ######    ######   #####   ######  #     #\n\n                           -powered by Gianluca Figini")
sleep(5)
#Briscola
def newgame():
    val =["2","4","5","6","7","donna","cavallo","re ","tre","asso "] #Definizione dei valori
    sem =["bastoni","coppe","spade","denari "] #Definizione dei semi
    pes = [] #Carte pescate
    mano = [] #Mano player
    cmano = [] #Mano computer
    def draw(): #Funzione per pescare (player)
        a = len(mano)
        while a<3:
            x = randint(0,9)
            y = randint(0,3)
            if not [x,y] in pes:
                pes.append([x,y])
                mano.append([x,y])
                a = a+1
    def cdraw(): #Funzione per pescare (computer)
        ca = len(cmano)
        while ca<3:
            x = randint(0,9)
            y = randint(0,3)
            if not [x,y] in pes:
                pes.append([x,y])
                cmano.append([x,y])
                ca = ca+1
    def cshow(): #Funzione per mostrare le carte (computer)
        print("\nMano computer")
        for x in range(3):
            try:
                print("  ("+str(x+1)+") "+val[cmano[x][0]]+" di "+sem[cmano[x][1]])
            except IndexError:
                print("  (*) slot vuoto")
    def show(): #Funzione per mostrare le carte (mano)
        print("La tua mano:")
        for x in range(3):
            try:
                print("  ("+str(x+1)+") "+val[mano[x][0]]+" di "+sem[mano[x][1]])
            except IndexError:
                print("  (*) slot vuoto")
    b = randint(0,3) #Selezione briscola
    player = 0 #Punti player
    computer = 0 #Punti computer
    print('\n'*50+"***La briscola é "+sem[b]+"***\n")
    win = 0 #Valore vittoria ultima mano (0=vinta, 1=persa)
    for c in range(20):
        if win == 0:                                                            #Se hai vinto la scorsa mano
            if len(pes)!=40:
                draw()
                cdraw()
            show()
            print("\n  Briscola: "+str(sem[b]))
            while True:             #Inserire l'indice della carta
                mano1 = int(input("Indice carta: "))
                try:
                    if mano1 == 120100:
                        cshow()
                    else:
                        x = mano[mano1-1][0]
                        y = mano[mano1-1][1]
                        play=[x,y]
                        del mano[mano1-1]
                        break
                except IndexError:
                    print("\n***ERRORE: Questa carta non è nella tua mano***\n")
                except ValueError:
                    print('\n***ERRORE: Indice non valido***\n')
            print('\n'*15)
            if x == val.index("donna"): #Punti giocati
                punti = 2
            elif x == val.index("cavallo"):
                punti = 3
            elif x ==val.index("re "):
                punti = 4
            elif x ==val.index("tre"):
                punti = 10
            elif x == val.index("asso "):
                punti = 11
            else:
                punti = 0
            cmano1 = -1                                                           #play computer
            if punti >9:#se player ha giocato asso o tre non di briscola, computer gioca la briscola più bassa che ha in mano se ne ha almeno una
                for r in range(len(cmano)):
                    if cmano[r][1] == b and y != b and not cmano in [0,1,2]:
                        cmano1 = r
                    elif cmano[r][1] == b and y != b:
                        if cmano[cmano1][0] > cmano[r][0]:
                            cmano1 = r
                    elif cmano[r][1] == b and y == b and cmano[r][0]>x:
                        cmano1 = r
            elif y == b:#Se player ha giocato una briscola gioca la carta più bassa possibile
                for r in range(len(cmano)):
                    if cmano1 == -1:
                        cmano1 = r
                    elif cmano[r][0] < cmano[cmano1][0]:
                        cmano1 = r
            for r in range(len(cmano)):#Se computer ha un carico dello stesso seme non briscola, cerca di superare
                if y == cmano[r][1] and  7 <= cmano[r][0] and y != b and not cmano1 in range(3):
                    cmano1 = r
            if not cmano1 in [0,1,2]:#altrimenti la più piccola carta non briscola o carico
                for r in range(len(cmano)):
                    if not cmano1 in [0,1,2] and cmano[r][1] != b and cmano[r][0]<9:
                        cmano1 = r
                    elif cmano[r][0] < cmano[cmano1][0] and cmano[r][1] != b and cmano[r][0]<9:
                        cmano1 = r
            if not cmano1 in [0,1,2]:#altrimenti la più piccola carta  briscola
                for r in range(len(cmano)):
                    if not cmano1 in [0,1,2]:
                        cmano1 = r
                    elif cmano[r][0] < cmano[cmano1][0]:
                        cmano1 = r
            cplay = cmano[cmano1]
            del cmano[cmano1]
            if cplay[0]==val.index("asso "): #Punti giocati computer
                cpunti = 11
            elif cplay[0] == val.index("tre"):
                cpunti = 10
            elif cplay[0] == val.index("re "):
                cpunti = 4
            elif cplay[0] == val.index("cavallo"):
                cpunti = 3
            elif cplay[0] == val.index("donna"):
                cpunti = 2
            else:
                cpunti = 0
            print('\n'+'-'*30+'|'+'-'*30) #tabellina
            print("            PLAYER            |            COMPUTER            ")
            print(''+'-'*30+'|'+'-'*30)
            print(' '*int((15-len(val[play[0]])/2)+0.5)+val[play[0]]+' '*int((15-len(val[play[0]])/2)-0.5)+'|'+' '*int((15-len(val[cplay[0]])/2)+0.5)+val[cplay[0]])
            print(' '*int((15-len(sem[play[1]])/2)+0.5)+sem[play[1]]+' '*int((15-len(sem[play[1]])/2)-0.5)+'|'+' '*int((15-len(sem[cplay[1]])/2)+0.5)+sem[cplay[1]])
            print('-'*30+'|'+'-'*30)
        else:                                                                   #se hai perso la scorsa mano
            if len(pes)!=40:
                cdraw()
                draw()
            show()
            cmano1 = -1
            for r in range(len(cmano)):                                     #computer gioca la carta più bassa non briscola, se possibile
                if cmano1== -1 and cmano[r][1] != b:
                    cmano1 = r
                elif cmano[r][0]<cmano[cmano1][0]and cmano[r][1] != b:
                    cmano1 = r
            if cmano1== -1:
                for r in range(len(cmano)):                                 #altrimenti la briscola più bassa
                    if cmano1== -1:
                        cmano1 = r
                    elif cmano[r][0]<cmano[cmano1][0]:
                        cmano1 = r
            cplay = cmano[cmano1]
            del cmano[cmano1]
            if cplay[0]==val.index("asso "): #Calcolo punti giocati
                cpunti = 11
            elif cplay[0] == val.index("tre"):
                cpunti = 10
            elif cplay[0] == val.index("re "):
                cpunti = 4
            elif cplay[0] == val.index("cavallo"):
                cpunti = 3
            elif cplay[0] == val.index("donna"):
                cpunti = 2
            else:
                cpunti = 0
            print('\n'+'-'*30+'|'+'-'*30) #Tabellina
            print("            COMPUTER          |            PLAYER            ")
            print('-'*30+'|'+'-'*30)
            print(' '*int(15-len(val[cplay[0]])/2+0.5)+val[cplay[0]]+' '*int(15-len(val[cplay[0]])/2-0.5)+'|'+' '*15+'?'+' '*(14))
            print(' '*int(15-len(sem[cplay[1]])/2+0.5)+sem[cplay[1]]+' '*int(15-len(sem[cplay[1]])/2-0.5)+'|'+' '*15+'?'+' '*(14))
            print('-'*30+'|'+'-'*30)
            print("\n  Briscola: "+str(sem[b]))
            while True:
                mano1 = int(input("Indice carta: "))
                try:
                    if mano1 == 120100:
                        cshow()
                    else:
                        x = mano[mano1-1][0]
                        y = mano[mano1-1][1]
                        del mano[mano.index([x,y])]
                        break
                except IndexError:
                    print("\n***ERRORE: Questa carta non è nella tua mano***\n")
                except ValueError:
                    print('\n***ERRORE: Indice non valido***\n')
            print('\n'*15)
            if x == val.index("donna"):
                punti = 2
            elif x == val.index("cavallo"):
                punti = 3
            elif x ==val.index("re "):
                punti = 4
            elif x ==val.index("tre"):
                punti = 10
            elif x == val.index("asso "):
                punti = 11
            else:
                punti = 0
        if (cplay[1]!=y and cplay[1]!= b and win == 0) or (cplay[1]!=y and y== b) or (cplay[1]==y and cplay[0]<x):
            player = player + punti + cpunti
            win = 0
        elif (cplay[1]!=y and y!= b and win == 1) or (cplay[1]!=y and cplay[1]== b) or (cplay[1]==y and cplay[0]>x):
            computer = computer + punti + cpunti
            win = 1
        if win == 0:
            print("\n","***Mano vinta!***\n\nPunti vinti:   "+str(punti+cpunti))
        else:
            print("\n***Mano persa!***\n\nPunti persi:   "+str(punti+cpunti))
        print("Mani restanti: "+str(19-c)+"\n")
    if player>computer:
        print("        #     # ##### ####### #######  #####   ######  #####    #\n        #     #   #      #       #    #     #  #     #   #     # #\n        #     #   #      #       #    #     #  #     #   #    #   #\n        #     #   #      #       #    #     #  ######    #   #     #\n         #   #    #      #       #    #     #  #   #     #   #######\n          # #     #      #       #    #     #  #    #    #   #     #\n           #    #####    #       #     #####   #     # ##### #     #\n\n"+str(player)+":"+str(computer))
    elif player == computer:
        print("    ######     #    ####### #######    #\n    #     #   # #      #       #      # #\n    #     #  #   #     #       #     #   #\n    ######  #     #    #       #    #     #\n    #       #######    #       #    #######\n    #       #     #    #       #    #     #\n    #       #     #    #       #    #     #\n\n60:60")
    else:
        print("         ######   ######   #####  #     #  ####### ##### ####### #######    #\n        #        #        #     # ##    #  #         #      #       #      # #\n        #        #        #     # # #   #  #         #      #       #     #   #\n         #####   #        #     # #  #  #  ######    #      #       #    #     #\n              #  #        #     # #   # #  #         #      #       #    #######\n              #  #        #     # #    ##  #         #      #       #    #     #\n        ######    ######   #####  #     #  #       #####    #       #    #     #\n\n"+str(player)+":"+str(computer))
    print("\n\nLa funzione 'newgame()' permetter di riavviare il gioco")
    sleep(5)

newgame()
