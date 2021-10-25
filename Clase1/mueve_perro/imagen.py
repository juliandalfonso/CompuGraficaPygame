import pygame
from pygame.locals import*
from os import path
working_dir = path.dirname(__file__)
#Escritorio/PYGAME/Sprites/F9/CartoonViking/Attack01

ANCHOPANTALLA=1280
ALTOPANTALLA=640
NEGRO = [0,0,0]
BLANCO = [255,255,255]
ROJO = [255,0,0]
VERDE = [0,255,0]
AZUL = [0,0,255]
AMARILLO = [255,255,0]




if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHOPANTALLA,ALTOPANTALLA])
    back= 'Back.png'

    FONDO = pygame.image.load(path.join(working_dir,back)).convert()
    centro=[300,200]  #centro de la pantalla
    pygame.display.flip()
    Img = pygame.image.load(path.join(working_dir, 'howl.png'))

    #pantalla.fill(NEGRO)

    #proceso a continuacion
    x=0
    y=0
    ix = 0
    iy = 0
    posxaux=0
    posyaux=500
    posx = 0
    posy= 0
    velx=10
    vely=2
    jumping=False
    jumpaux=0
    salto=400

    fin = False
    reloj = pygame.time.Clock()
    pygame.display.flip()

    while not fin:
        reloj.tick(20)
        for event in pygame.event.get():
            if event.type == QUIT:
                fin = True
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    ix = +velx
                    iy = 0
                    if posxaux<=0:
                        posxaux=0
                    elif  posxaux>0:
                        posx -= velx
                if event.key == K_RIGHT:
                    ix = -velx
                    iy = 0
                    if posxaux>=ANCHOPANTALLA/2-64:
                        posx=0
                        posxaux=ANCHOPANTALLA/2-64
                    elif posxaux<ANCHOPANTALLA:
                        posx += velx
                if event.key == K_UP:
                    if posyaux==500:
                        print "posyaux==500"
                        if  jumping==False:
                            print "jumping falso"
                            jumping=True

            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    ix = 0
                    iy = 0
                    if posxaux>=ANCHOPANTALLA/2-64:
                        posx=0
                        posxaux=ANCHOPANTALLA/2-64
                    elif posxaux<ANCHOPANTALLA/2-64:
                        posx = 0

                if event.key == K_LEFT:
                    ix = 0
                    iy = 0
                    if posxaux<0:
                        posxaux=0
                        posx=0
                    elif  posxaux>0:
                        posx = 0

        if jumping:
            print "entra una"
            posyaux-=10
            if jumpaux<=400:
                print "entra dos"
                jumping=False
        elif jumpaux>=500 and jumping==False:
            print "entra tres"
            posyaux+=10

        '''
                posyaux-=10
            if posyaux<=salto:
                posyaux+=10
                if posyaux>=500:
                    jumping=False


            elif posyaux<500 and jumping==False:
                posyaux+=3
-        '''

        x += ix
        y += iy
        posxaux += posx
        posyaux += posy
        rel_x = x % FONDO.get_rect().width
        pantalla.blit(FONDO,[rel_x - FONDO.get_rect().width,y])
        if rel_x < ANCHOPANTALLA:
            pantalla.blit(FONDO,[rel_x,y])
        pantalla.blit(Img,[posxaux,posyaux])

        pygame.display.flip()
