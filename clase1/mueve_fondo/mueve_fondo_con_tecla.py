import pygame
from os import path
working_dir = path.dirname(__file__)


ANCHOPANTALLA=600
ALTOPANTALLA=400
NEGRO = [0,0,0]
BLANCO = [255,255,255]
ROJO = [255,0,0]
VERDE = [0,255,0]
AZUL = [0,0,255]
AMARILLO = [255,255,0]

if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHOPANTALLA,ALTOPANTALLA])
    imagen = 'FONDO.jpg'
    FONDO = pygame.image.load(path.join(working_dir,imagen))
    x=0
    y=0
    ix = 0
    iy = 0
    reloj = pygame.time.Clock()


    centro=[300,200]  #centro de la pantalla

    #pantalla.fill(NEGRO)

    fin = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ix = -2
                    iy = 0
            #if event.type == pygame.KEYUP:
            #    if event.key == pygame.K_RIGHT:
            #        ix = 0
            #        iy = 0


        print(ix)
        x += ix
        y += iy

        pantalla.fill(NEGRO)
        pantalla.blit(FONDO,[x,y])
        pygame.display.flip()
        reloj.tick(20)
