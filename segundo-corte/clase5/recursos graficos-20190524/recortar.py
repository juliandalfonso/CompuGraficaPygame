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
    col=16
    fil=3

    cuadro= img.subsurface(col*an_c,fil*al_c,32,32)
    pantalla.blit(cuadro,[0,0])
    pygame.display.flip()
    fin = False
    while not fin:
        #reloj.tick(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
