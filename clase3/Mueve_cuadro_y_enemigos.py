import pygame
import Repo as rep
import random
'''
pasos para adicionar objtos
1 crear la Clase
2 crear el grupo
3crear el objeto e instanciar la clase
'''




class Cuadro(pygame.sprite.Sprite):
    '''
    Clase Cuadro
    '''
    def __init__(self,p,cl=rep.BLANCO):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([40,50])
        self.image.fill(cl)
        self.rect=self.image.get_rect()
        self.rect.x=p[0]
        self.rect.y=p[1]
        self.velx=0
        self.vely=0

    def update(self):    #le permite al pobjeto actualizar su estado
        self.rect.x +=self.velx
        self.rect.y +=self.vely


class Bala(pygame.sprite.Sprite):
    '''
    Clase Bala
    '''
    def __init__(self,p,cl=rep.BLANCO):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([10,10])
        self.image.fill(cl)
        self.rect=self.image.get_rect()
        self.rect.x=p[0]
        self.rect.y=p[1]
        self.velx=0
        self.vely=9

    def update(self):    #le permite al pobjeto actualizar su estado
        self.rect.y-=self.vely



class Rival(pygame.sprite.Sprite):
    '''
    Clase Rival
    '''
    def __init__(self,p,cl=rep.RED):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([30,40])
        self.image.fill(cl)
        self.rect=self.image.get_rect()
        self.rect.x=p[0]
        self.rect.y=p[1]
        self.velx=3

    def update(self):    #le permite al pobjeto actualizar su estado
        self.rect.x +=self.velx





if __name__ == '__main__':
    pygame.init()
    reloj=pygame.time.Clock()
    pantalla=pygame.display.set_mode([rep.ANCHOPANTALLA,rep.ALTOPANTALLA])
    jugadores=pygame.sprite.Group()
    Rivales=pygame.sprite.Group()
    Balas=pygame.sprite.Group()
    j1=Cuadro([270,350],rep.GREEN)
    jugadores.add(j1)


    #Codigo
    n=10
    for i in range(n):
        r=Rival([20,20])
        r.rect.x=-1*random.randrange(150)
        r.rect.y=random.randrange(400)
        r.velx=random.randrange(10)
        Rivales.add(r)
    ptos=0
    #Codigo
    reloj=pygame.time.Clock()
    pygame.display.flip()
    fin = False
    while not fin:
        #reloj.tick(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    j1.velx=5
                if event.key == pygame.K_LEFT:
                    j1.velx=-5
                if event.key == pygame.K_DOWN:
                    j1.vely=5
                if event.key == pygame.K_UP:
                    j1.vely=-5
                if event.key == pygame.K_SPACE:
                    b=Bala([j1.rect.x,j1.rect.y],rep.YELLOW)
                    Balas.add(b)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    j1.velx=0
                if event.key == pygame.K_LEFT:
                    j1.velx=0
                if event.key == pygame.K_DOWN:
                    j1.vely=0
                if event.key == pygame.K_UP:
                    j1.vely=0



        for r in Rivales:
            if r.rect.x>=(rep.ANCHOPANTALLA-r.rect.width):
                r.rect.x=rep.ANCHOPANTALLA-r.rect.width
                r.velx=-random.randrange(10)
            if r.rect.x<=0:
                r.rect.x=0
                r.velx=random.randrange(10)
        #control
        #print(j1.rect.left,j1.rect.right,j1.rect.top,j1.rect.bottom) #imprime las posiciones del sprite o rectangulo
        #print(j1.rect.width,j1.rect.height) #imprime la altura y ancho del sprite u objeto
        if j1.rect.x>(rep.ANCHOPANTALLA-j1.rect.width):
            j1.rect.x=rep.ANCHOPANTALLA-j1.rect.width
            j1.velx=0
        if j1.rect.x<0:
            j1.rect.x=0
            j1.velx=0
        if j1.rect.bottom>=rep.ALTOPANTALLA:
            j1.rect.bottom=rep.ALTOPANTALLA



        #control
        if j1.rect.x>(rep.ANCHOPANTALLA-j1.rect.width):
            pass

        for r in Rivales:
            pass

        for b in Balas:
            ls_col=pygame.sprite.spritecollide(b,Rivales,True)
            for r in ls_col:
                ptos+=1
                print ptos
                Balas.remove(b)
                '''
        #limpieza
        for b in Balas:
            if b.rect.y<-10:
                balas.remove(b)
        '''
        jugadores.update()
        Rivales.update()
        Balas.update()
        #Refresco de pantalla
        pantalla.fill(rep.NEGRO)
        Rivales.draw(pantalla)
        jugadores.draw(pantalla)
        Balas.draw(pantalla)
        pygame.display.flip()
        reloj.tick(30)
