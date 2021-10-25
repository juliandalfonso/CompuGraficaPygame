import pygame
import Repo as rep
import random
'''
pasos para adicionar objtos
1 crear la Clase
2 crear el grupo
3crear el objeto e instanciar la clase
4 dibujarlo
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
        self.bombas=0

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
        self.rect.y+=self.vely


class Balas_r(pygame.sprite.Sprite):
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
        #self.velx=0
        self.vely=0

    def update(self):    #le permite al pobjeto actualizar su estado
        self.rect.y+=self.vely



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
        self.temp=0

    def update(self):    #le permite al pobjeto actualizar su estado
        self.rect.x +=self.velx


class Ventaja(pygame.sprite.Sprite):
    '''
    Clase Ventaja
    '''
    def __init__(self,p,cl=rep.AZUL):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([15,15])
        self.image.fill(cl)
        self.rect=self.image.get_rect()
        self.rect.x=p[0]
        self.rect.y=p[1]
        self.velx=5
        self.vely=5

    def update(self):    #le permite al pobjeto actualizar su estado
        self.rect.y += self.vely
        if self.rect.y>=(rep.ALTOPANTALLA-self.rect.height):
            self.rect.y=rep.ALTOPANTALLA-self.rect.height
            self.vely=0




if __name__ == '__main__':
    pygame.init()
    reloj=pygame.time.Clock()
    pantalla=pygame.display.set_mode([rep.ANCHOPANTALLA,rep.ALTOPANTALLA])
    Jugadores=pygame.sprite.Group()
    Rivales=pygame.sprite.Group()
    Balas=pygame.sprite.Group()
    balas_r=pygame.sprite.Group()
    Ventajas=pygame.sprite.Group()
    j1=Cuadro([270,350],rep.GREEN)
    Jugadores.add(j1)


    #Codigo
    n=10
    for i in range(n):
        r=Rival([20,20])
        r.rect.x=random.randrange(rep.ANCHOPANTALLA)
        r.rect.y=random.randrange(rep.ALTOPANTALLA-100)
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
            if event.type == (pygame.QUIT):
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
                    b=Bala([j1.rect.x+j1.rect.width/2,j1.rect.y],rep.YELLOW)
                    b.vely=-7
                    Balas.add(b)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    j1.velx=0
                    j1.vely=0
                if event.key == pygame.K_LEFT:
                    j1.velx=0
                    j1.vely=0
                if event.key == pygame.K_DOWN:
                    j1.vely=0
                if event.key == pygame.K_UP:
                    j1.vely=0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if j1.bombas>=1:
                        for r in Rivales:
                            Rivales.remove(r)
                        j.bombas-=1
                    else: print"no te quedan bombas"



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
            if r.temp<=0:
                b=Bala([r.rect.x,r.rect.y],rep.ROJO)
                b.vely=7
                balas_r.add(b)
                r.temp=random.randrange(100)

        for b in Balas:
            ls_col=pygame.sprite.spritecollide(b,Rivales,True)
            for r in ls_col:
                ptos+=1
                #r=Rival([100,100],rep.AMARILLO)
                #r.rect.x=-1*random.randrange(150)
                #r.rect.y=random.randrange(300)
                #r.velx=random.randrange(10)
                #Rivales.add(r)
                si_ventaja = random.randrange(1000)
                if si_ventaja>600:
                    #crear Ventaja
                    v=Ventaja ([r.rect.x+r.rect.width,r.rect.y ],rep.AZUL)
                    Ventajas.add(v)
                print "puntos: ",ptos
                Balas.remove(b)

        for j in Jugadores:
            ls_cap=pygame.sprite.spritecollide(j,Ventajas,True)
            for v in ls_cap:
                j1.bombas +=1
                Ventajas.remove(v)
                print"Bombas: ",j1.bombas


        #limpieza
        for b in Balas:
            if b.rect.y<-10:
                Balas.remove(b)


        Jugadores.update()
        Rivales.update()
        Balas.update()
        Ventajas.update()
        balas_r.update()
        #Refresco de pantalla
        pantalla.fill([20,20,20])
        Rivales.draw(pantalla)
        Jugadores.draw(pantalla)
        Balas.draw(pantalla)
        balas_r.draw(pantalla)
        Ventajas.draw(pantalla)
        pygame.display.flip()
        reloj.tick(30)
