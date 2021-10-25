import pygame
import Repo as rep

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

class Bala(pygame.sprite.Sprite):
    '''
    Clase Bala
    '''
    def __init__(self,p,cl=rep.BLANCO):
    #def __init__(self,p,cl=rep.BLANCO,baly,balx):
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
        #self.rect.y+=baly
        #self.rect.x+=balx


def BuscaJugador(PJx,PJy,PEx,PEy):
    '''
    PJ: es la posicion del jugador
    PE: es la posicion del enemigo
    y = mx + b
    m = (PJ[1]-PE[1])/(PJ[0]-PJ[1])
    '''
    if(PJx-PEx)!=0:
        m = ((PJy-PEy)/(PJx-PEx))
        b = (PEy-(m*PEx))
        y = (m*PJx)+b
        return y




if __name__ == '__main__':
    pygame.init()
    reloj=pygame.time.Clock()
    pantalla=pygame.display.set_mode([rep.ANCHOPANTALLA,rep.ALTOPANTALLA])
    jugadores=pygame.sprite.Group()
    bloques = pygame.sprite.Group()
    j1=Cuadro([270,100],rep.GREEN)
    bl=Bloque([300,100],[30,90],rep.BLANCO)
    bl2=Bloque([360,200],[90,30],rep.BLANCO)
    jugadores.add(j1)
    bloques.add(bl)
    #bloques.add(bl2)
    Balas=pygame.sprite.Group()



    reloj=pygame.time.Clock()

    #Codigo

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
                    j1.velx=0
                    j1.vely=0

                if event.key == pygame.K_x:
                    finalretorno = BuscaJugador(j1.rect.x,j1.rect.y,bl.rect.x,bl.rect.y)
                    #b=Bala([bl.rect.x+bl.rect.width/2,bl.rect.y],rep.YELLOW,baly,balx)
                    b=Bala([bl.rect.x,bl.rect.y],rep.YELLOW)
                    if(j1.rect.y>bl.rect.y):
                        b.vely=7
                    else:
                        b.vely=-7
                    b.rect.y=finalretorno
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
                    j1.velx=0
                if event.key == pygame.K_UP:
                    j1.vely=0
                    j1.velx=0
                if event.key == pygame.K_SPACE:
                    j1.velx=0
                    j1.vely=0

        #control
        #print(j1.rect.left,j1.rect.right,j1.rect.top,j1.rect.bottom) #imprime las posiciones del sprite o rectangulo
        #print(j1.rect.width,j1.rect.height) #imprime la altura y ancho del sprite u objeto
        if j1.rect.x>(rep.ANCHOPANTALLA-j1.rect.width):
            j1.rect.x=rep.ANCHOPANTALLA-j1.rect.width
            j1.velx=0
        if j1.rect.x<0:
            j1.rect.x=0
            j1.velx=0

        for bl in bloques:
            ls = pygame.sprite.spritecollide(j1,bloques,False)
            for e in ls:
                if j1.rect.right > e.rect.left:
                    if(j1.velx>0):
                        j1.rect.right = e.rect.left
                        j1.velx=0

                if j1.rect.left < e.rect.right:
                    if(j1.velx<0):
                        j1.rect.left = e.rect.right
                        j1.velx=0
                if j1.rect.bottom > e.rect.top:
                    if(j1.vely>0):
                        j1.rect.bottom = e.rect.top
                        j1.vely=0
                if j1.rect.top < e.rect.bottom:
                    if(j1.vely<0):
                        j1.rect.top = e.rect.bottom
                        j1.vely=0


        jugadores.update()
        Balas.update()
        #Refresco de pantalla
        pantalla.fill(rep.NEGRO)
        jugadores.draw(pantalla)
        bloques.draw(pantalla)
        Balas.draw(pantalla)
        pygame.display.flip()
        reloj.tick(30)
