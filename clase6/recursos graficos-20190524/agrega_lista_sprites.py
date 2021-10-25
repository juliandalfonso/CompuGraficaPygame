import pygame
import Repo as rep
from os import path
working_dir = path.dirname(__file__)


if __name__ == '__main__':
    pygame.init()
    reloj=pygame.time.Clock()
    pantalla=pygame.display.set_mode([rep.ANCHOPANTALLA,rep.ALTOPANTALLA])
    img=pygame.image.load('terrenogen.png')

    #Codigo
    an_c=32
    al_c=32
    col=0
    fil=0
    numcol=32
    numfil=12
    ls=[]
    cont=0

    for i in range(numfil):
        for j in range(numcol):
            cuadro=img.subsurface(j*an_c,i*al_c,32,32)
            ls[i][j]=cuadro

    print ls

    '''while col<numcol:
        while fil<numfil:
            cuadro=img.subsurface(col*an_c,fil*al_c,32,32)

            col+=1
        fil+=1
        print fil'''




    #cuadro= img.subsurface(col*an_c,fil*al_c,32,32)

    pantalla.blit(cuadro,[0,0])
    #print cuadro
    pygame.display.flip()
    fin = False
    while not fin:
        #reloj.tick(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
