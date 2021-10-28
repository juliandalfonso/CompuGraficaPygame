import pygame
import Repo as rep

class Cuadro(pygame.sprite.Sprite):
    '''
    Clase Cuadro
    '''
    def __init__(self,pos,cl=rep.BLANCO):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([40,50])
        self.image.fill(cl)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0
        #self.jumping=False

    def update(self):    #le permite al pobjeto actualizar su estado
        self.rect.x +=self.velx
        self.rect.y +=self.vely


if __name__ == '__main__':
    pygame.init()
    reloj=pygame.time.Clock()
    pantalla=pygame.display.set_mode([rep.ANCHOPANTALLA,rep.ALTOPANTALLA])
    jugadores=pygame.sprite.Group()
    j1=Cuadro([0,rep.ALTOPANTALLA-50],rep.GREEN)
    j2=Cuadro([200,250],rep.BLUE)
    jugadores.add(j1)
    jugadores.add(j2)
    jumping=False






    #Codigo

    pygame.display.flip()
    reloj=pygame.time.Clock()
    fin = False
    while not fin:
        #reloj.tick(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    j1.velx=5
                    j1.vely=0
                if event.key == pygame.K_LEFT:
                    j1.velx=-5
                    j1.vely=0
                if event.key == pygame.K_s:
                    j1.velx=0
                    j1.vely=0
                if event.key == pygame.K_DOWN:
                    j1.vely=5
                    j1.velx=0
                if event.key == pygame.K_UP:
                    j1.vely=-5
                    j1.velx=0
                if event.key == pygame.K_SPACE:
                    print"jumping true"
                    jumping=True


        #control
        #print(j1.rect.left,j1.rect.right,j1.rect.top,j1.rect.bottom) #imprime las posiciones del sprite o rectangulo
        #print(j1.rect.width,j1.rect.height) #imprime la altura y ancho del sprite u objeto
        if j1.rect.x>(rep.ANCHOPANTALLA-j1.rect.width):
            j1.rect.x=rep.ANCHOPANTALLA-j1.rect.width
            j1.velx=0
        if j1.rect.x<0:
            j1.rect.x=0
            j1.velx=0
        if j1.rect.bottom>rep.ALTOPANTALLA:
            j1.rect.bottom=rep.ALTOPANTALLA
            j1.vely=0
        if jumping:
            print j1.rect.top
            print j2.rect.bottom
            if (j1.rect.bottom>rep.ALTOPANTALLA or j1.rect.bottom<=rep.ALTOPANTALLA-150 or j1.rect.top<=j2.rect.bottom):
                if (j1.rect.top<=j2.rect.bottom and ((j1.rect.x>=j2.rect.x and j1.rect.x<=(j2.rect.x+j2.rect.width))) or ((j1.rect.x+j1.rect.width>=j2.rect.x)and(((j1.rect.x+j1.rect.width)<=(j2.rect.x+j2.rect.width))))):
                    j1.vely=0
                    print "entramos papu"
                jumping=False
            elif j1.rect.bottom<=rep.ALTOPANTALLA and  jumping==True:
                j1.vely -=10
        if j1.rect.bottom<rep.ALTOPANTALLA and jumping==False:
            j1.vely+=5
            if j1.rect.bottom>=rep.ALTOPANTALLA:
                j1.rect.bottom=rep.ALTOPANTALLA

        jugadores.update()
        #Refresco de pantalla
        pantalla.fill(rep.NEGRO)
        jugadores.draw(pantalla)
        pygame.display.flip()
        reloj.tick(30)
