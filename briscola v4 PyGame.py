import pygame
from random import randint
from time import sleep

class Carta:
    valori = ['due', 'quattro', 'cinque', 'sei', 'sette', 'donna', 'cavaliere', 're', 'tre', 'asso']
    semi = ['bastoni', 'coppe', 'denari', 'spade']

    def __init__(self, val, sem):
        self.valore = val
        self.seme = sem
        self.punti = self.score(val)
    
    def getImage(self):
        nome = self.valori[self.valore] + '_' + self.semi[self.seme] +'.jpg'
        ans =pygame.image.load('C:/Users/Gianluca Figini/Pictures/carte_napoletane/' + nome)
        return pygame.transform.scale(ans, (150, 234))

    def score(self, val):
        if val == 9:
            return 11
        if val == 8:
            return 10
        if val == 7:
            return 4
        if val == 6:
            return 3
        if val == 5:
            return 2
        return 0




class Briscola:
    def __init__ (self):
        self.mazzo = []
        self.manoP = []
        self.manoC = []
        self.puntiP = 0
        self.puntiC = 0
        self.briscola = randint(0,3)
        self.maniGiocate = 0
        self.comincia = True
        self.tavoloP = None
        self.tavoloC = None

        self.start()
    
    def start(self):
        for i in range(10):
            for j in range(4):
                self.mazzo.append(Carta(i, j))
        self.pesca(True)
        self.pesca(False)
    
    def pesca(self, player):
        if player == True:
            while len(self.manoP) < 3 and len(self.mazzo) > 0:
                x = randint(0, len(self.mazzo) -1)
                self.manoP.append(self.mazzo[x])
                del self.mazzo[x]
        else:
            while len(self.manoC) < 3 and len(self.mazzo) > 0:
                x = randint(0, len(self.mazzo) -1)
                self.manoC.append(self.mazzo[x])
                del self.mazzo[x]
    
    def play(self, player, carta):
        if player == True:
            self.tavoloP = self.manoP[carta]
            del self.manoP[carta]
        else:
            self.tavoloC = self.manoC[carta]
            del self.manoC[carta]

    def chiudiMano(self):
        if ((self.tavoloC.seme == self.briscola and self.tavoloP.seme != self.briscola) or
            (self.tavoloC.seme == self.tavoloP.seme and self.tavoloC.valore > self.tavoloP.valore) or
            (self.tavoloC.seme != self.tavoloP.seme and self.tavoloP.seme != self.briscola and not self.comincia)):
            self.puntiC += self.tavoloC.punti + self.tavoloP.punti
            self.comincia = False
        else:
            self.puntiP += self.tavoloC.punti + self.tavoloP.punti
            self.comincia = True
        self.tavoloC = self.tavoloP = None
        self.pesca(True)
        self.pesca(False)
        self.maniGiocate += 1

    def liscio(self, player):
        if player:
            mano = self.manoP
        else:
            mano = self.manoC
        ans = -1
        for i in range(len(mano)):
            if ((ans == -1 and mano[i].valore < 8 and mano[i].seme != briscola) or
                (ans != -1 and mano[i].valore < mano[ans].valore and mano[i].seme != briscola)):
                ans = i
        if ans != -1:
            return ans
        for i in range(len(mano)):
            if ((ans == -1 and mano[i].valore < 8) or
                (ans != -1 and mano[i].valore < mano[ans].valore)):
                ans = i
        if ans != -1:
            return ans
        for i in range(len(mano)):
            if ((ans == -1 and mano[i].seme != self.briscola) or
                (ans != -1 and mano[i].valore < mano[ans].valore and mano[i].seme != briscola)):
                ans = i
        if ans != -1:
            return ans
        ans = 0
        for i in range(len(mano)):
            if mano[i].valore < mano[ans].valore:
                ans = i
        return ans

    def briscolino(self, player):
        if player:
            mano = self.manoP
        else:
            mano = self.manoC
        ans = -1
        for i in range(len(mano)):
            if ((ans == -1 and mano[i].seme == self.briscola) or
                (ans != -1 and mano[i].valore < mano[ans].valore and mano[i].seme == self.briscola)):
                ans = i
        if ans != -1:
            return ans
        else:
            return self.liscio(player)

    def carico(self, player):
        if player:
            mano = self.manoP
        else:
            mano = self.manoC
        ans = -1
        for i in range(len(mano)):
            if ((ans == -1 and mano[i].valore >= 8 and mano[i].seme != self.briscola) or
                (ans != -1 and mano[i].valore > mano[ans].valore and mano[i].seme !=self.briscola)):
                ans = i
        if ans != -1:
            return ans
        else:
            return self.liscio(player)

    def supera(self, player, carta):
        if player:
            mano = self.manoP
        else:
            mano = self.manoC
        ans = -1
        for i in range(mano):
            if ((ans == -1 and mano[i].seme == carta.seme and mano[i].valore > carta.valore) or
                (ans != -1 and mano[i].seme == carta.seme and mano[i],valore > mano[ans].valore)):
                ans = i
        return ans

    def getPlayC(self):
        play = -1
        if self.tavoloP == None:
            play = self.liscio(False)
        else: 
            supera = self.supera(False, tavoloP)
            if self.tavoloP.valore >= 8:
                if supera != -1:
                    play = supera
                else:
                    play = self.briscolino(False)
            elif (self.tavoloP.seme != self.briscola and supera != -1 and self.manoC[supera].valore >= 8):
                play = supera
            else:
                play = self.liscio(False)


def main():
    SIZE = 900, 800
    window = pygame.display.set_mode((SIZE))
    pygame.display.set_caption('Briscola')
    newGame(window)

def newGame(window):
    briscola = Briscola()
    briscola.start()
    running = True
    FPS = 60
    clock = pygame.time.Clock()
    black = 0, 0, 0
    while briscola.maniGiocate < 20 and running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill(black)   
        drawWindow(window, briscola)
        if briscola.comincia:
            briscola.play(True, getPlay(window, briscola))


    pygame.quit()

def getPlay(window, briscola):
    end = False
    #while not end:
    #    drawWindow(window, briscola)


def drawWindow(window, briscola):
    black = 0, 0, 0
    red = 255, 0, 0
    
    for i in range(len(briscola.manoP)):
        image = briscola.manoP[i].getImage()
        image_rect = image.get_rect()
        mouse = pygame.mouse.get_pos()
        image_rect = image_rect.move([250 + i*160, 550])
        window.blit(image, image_rect)
        if mouse[0] > image_rect.left and mouse[0] < image_rect.right and mouse[1] > image_rect.top and mouse[1] < image_rect.bottom:
            pygame.draw.rect(window, red, image_rect, 5)

    for i in range(len(briscola.manoC)):
        image = pygame.image.load('C:/Users/Gianluca Figini/Pictures/carte_napoletane/back.png')
        image = pygame.transform.scale(image, (100, 156))
        window.blit(image, (300 + i*110, 50))

    if briscola.tavoloP != None:
        image = pygame.image.load(briscola.tavoloP.getImage())
        window.blit(image, (350, 200))

    if briscola.tavoloC != None:
        image = pygame.image.load(briscola.tavoloC.getImage())
        window.blit(image, (550, 200))

    
     
    pygame.display.update()



if __name__ == '__main__':
    main()



