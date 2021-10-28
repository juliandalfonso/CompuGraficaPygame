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

class Jugador(pygame.sprite.Sprite):
    '''
    Clase Jugador
    '''
    def __init__(self,p,cl=rep.BLANCO):
    #def __init__(self,id,p,cl=rep.BLANCO):

        pygame.sprite.Sprite.__init__(self)
        #self.id=id
        self.image=pygame.Surface([40,50])
        self.image.fill(cl)
        self.rect=self.image.get_rect()
        self.rect.x=p[0]
        self.rect.y=p[1]
        self.velx=0
        self.vely=0
        self.bombas=0
        self.vidas=3

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
        self.temp-=1

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



class Bloque(pygame.sprite.Sprite):
    '''
    Clase Bloque
    '''
    def __init__(self,p,dm,cl=rep.AZUL):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface(dm)
        self.image.fill(cl)
        self.rect=self.image.get_rect()
        self.rect.x=p[0]
        self.rect.y=p[1]
        self.vely=0

    def update(self):    #le permite al pobjeto actualizar su estado
        pass


if __name__ == '__main__':
    pygame.init()
    reloj=pygame.time.Clock()
    pantalla=pygame.display.set_mode([rep.ANCHOPANTALLA,rep.ALTOPANTALLA])
    jugadores=pygame.sprite.Group()
    rivales=pygame.sprite.Group()
    Balas=pygame.sprite.Group()
    balas_r=pygame.sprite.Group()
    Ventajas=pygame.sprite.Group()
    Bloques = pygame.sprite.Group()
    j1=Jugador([270,350],rep.GREEN)
    jugadores.add(j1)
    #ugadores.add(j2)


    #Codigo
    n=10
    for i in range(n):
        r=Rival([20,20])
        r.rect.x=random.randrange(rep.ANCHOPANTALLA)
        r.rect.y=random.randrange(rep.ALTOPANTALLA-100)
        r.velx=random.randrange(10)
        rivales.add(r)

    bl = Bloque([])

    fuente = pygame.font.Font(None,32)
    texto= fuente.render('Texto de Prueba', False, rep.BLANCO)
    ptos=0
    #Codigo
    reloj=pygame.time.Clock()
    fin_juego=False
    pygame.display.flip()
    fin = False
    while not (fin or fin_juego):
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
                        for r in rivales:
                            rivales.remove(r)
                        j.bombas-=1
                    else: print"no te quedan bombas"



        for r in rivales:
            if r.rect.x>=(rep.ANCHOPANTALLA-r.rect.width):
                r.rect.x=rep.ANCHOPANTALLA-r.rect.width
                r.velx=-random.randrange(10)
            if r.rect.x<=0:
                r.rect.x=0
                r.velx=random.randrange(10)
            if r.temp<0:
                b=Bala([r.rect.x,r.rect.y],rep.ROJO)
                b.vely=7
                balas_r.add(b)
                r.temp=random.randrange(100)

        if j1.rect.x>(rep.ANCHOPANTALLA-j1.rect.width):
            j1.rect.x=rep.ANCHOPANTALLA-j1.rect.width
            j1.velx=0
        if j1.rect.x<0:
            j1.rect.x=0
            j1.velx=0
        if j1.rect.bottom>=rep.ALTOPANTALLA:
            j1.rect.bottom=rep.ALTOPANTALLA


        for b in balas_r:
            ls_col=pygame.sprite.spritecollide(b,jugadores,True)
            if j in ls_col:
                if j.vidas==0:
                    fin_juego=True
                else:
                    vida_actual = j.vidas -1
                    print "vidas restantes: ",vida_actual+1
                    j1=Jugador([270,350],rep.VERDE)
                    j1.vidas=vida_actual
                    jugadores.add(j1)

        for b in Balas:
            ls_col=pygame.sprite.spritecollide(b,rivales,True)
            for r in ls_col:
                ptos+=1
                r=Rival([100,100],rep.AMARILLO)
                r.rect.x=-1*random.randrange(150)
                r.rect.y=random.randrange(300)
                r.velx=random.randrange(10)
                rivales.add(r)
                si_ventaja = random.randrange(1000)
                if si_ventaja>600:
                    #crear Ventaja
                    v=Ventaja ([r.rect.x+r.rect.width,r.rect.y ],rep.AZUL)
                    Ventajas.add(v)
                print "puntos: ",ptos
                Balas.remove(b)

        for j in jugadores:
            ls_cap=pygame.sprite.spritecollide(j,Ventajas,True)
            for v in ls_cap:
                j1.bombas +=1
                Ventajas.remove(v)
                print"Bombas: ",j1.bombas

        for bl in bloques:
            ls = pygame.sprite.spritecollide(j1,bloques,False)
            for e in ls:
                if j1.rect.right > e.rect.left:
                    j1.rect.right = e.rect.left
                    j1.velx=0


        #limpieza
        for b in Balas:
            if b.rect.y<-10:
                Balas.remove(b)


        jugadores.update()
        rivales.update()
        Balas.update()
        Ventajas.update()
        balas_r.update()
        #Refresco de pantalla
        pantalla.fill(rep.NEGRO)
        pantalla.blit(texto, [10,10])
        rivales.draw(pantalla)
        jugadores.draw(pantalla)
        Balas.draw(pantalla)
        balas_r.draw(pantalla)
        Ventajas.draw(pantalla)
        pygame.display.flip()
        reloj.tick(30)
    while not fin:
        for event in pygame.event.get():
            if event.type == (pygame.QUIT):
                fin = True
        pantalla.fill(rep.NEGRO)
        texto= fuente.render( 'GAME OVER', False, rep.BLANCO)
        pantalla.blit(texto, [250,200])
        pygame.display.flip()
