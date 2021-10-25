#Prueba matriz

import pygame
import math
import random
import Repo as rep

white=[255,255,255]
green=[0,255,0]
negro=[0,0,0]
red=[255,0,0]
blue=[0,10,200]
yellow=[247,255,0]

ANCHO=720
ALTO=720

def IRIS():
    return [random.randrange(255),random.randrange(255),random.randrange(255)]

def cut(img, columnasx, filas, an_c,al_c):
        imagenes = []
        for i in range(columnasx):
                imagenes.append([])

        for i in range(columnasx):
                for j in range(filas):
                        cuadro = img.subsurface(i*an_c, j*al_c, an_c, al_c)
                        imagenes[i].append(cuadro)

        return imagenes



class Jugador(pygame.sprite.Sprite):

        def __init__(self,mat_i,lim,pos_ini):
                pygame.sprite.Sprite.__init__(self)
                self.velx=0
                self.vely=0
                self.accion=0
                self.concol=0
                self.m=mat_i
                self.lim=lim
                self.image= self.m[self.concol][self.accion]
                self.rect=self.image.get_rect()
                self.rect.x=pos_ini[0]
                self.rect.y=pos_ini[1]
                self.estado=0


        def update(self):
                self.rect.x += self.velx
                self.rect.y += self.vely
                self.image= self.m[self.concol][self.accion]
                if self.concol < self.lim[self.accion]:
                        self.concol += 1
                else:
                        self.concol = 0

                        if self.accion != 1:
                                self.accion = 1

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
        self.velx=0

    def update(self):    #le permite al pobjeto actualizar su estado
        self.rect.x += self.velx
        if self.velx>0:
            self.velx-=1



if __name__ == '__main__':

        #Configuracion

        pantalla = pygame.display.set_mode([ANCHO,ALTO])
        img = pygame.image.load ('ken.png')

        # ESTO DEBE HACER LA FUNCION
        m = cut(img,7,10,70,80)

        lim=[3,3,2,4,0,3,4,4,5,0]

        jugadores = pygame.sprite.Group()
        j = Jugador(m,lim,[100,100])
        jugadores.add(j)

        bloques = pygame.sprite.Group()
        b=Bloque([150,100],[30,90],rep.BLANCO)
        bloques.add(b)

        #para cambiar la fila de la imagen..
        j.accion=1


        reloj=pygame.time.Clock()
        fin=False
        #Ciclo de juego o animacion
        while not fin:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                fin=True

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RIGHT:
                                    j.velx+=5
                                    j.vely=0

                            if event.key == pygame.K_LEFT:
                                    j.velx-=5
                                    j.vely=0

                            if event.key == pygame.K_UP:
                                    j.velx=0
                                    j.vely-=5

                            if event.key == pygame.K_DOWN:
                                    j.velx=0
                                    j.vely+=5

                            if event.key == pygame.K_c:
                                    j.accion=2
                                    j.concol=0

                            if event.key == pygame.K_v:
                                    j.accion=6
                                    j.concol=0
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_RIGHT:
                                j.velx=0
                                j.vely=0
                            if event.key == pygame.K_LEFT:
                                j.velx=0
                                j.vely=0


                for b in bloques:
                    pos_ken=[j.rect.right,j.rect.y]
                    if b.rect.collidepoint(j.rect.right,j.rect.y):
                        if j.accion==2:
                            b.velx=10
                        if j.accion==6:
                            b.velx=10




                jugadores.update()
                bloques.update()
                pantalla.fill(negro)
                jugadores.draw(pantalla)
                bloques.draw(pantalla)

                #pantalla.blit(m[col][accion],[100,100])
                pygame.display.flip()

                reloj.tick(10)


                '''
                if col <= lim[j.accion]:
                        col+=1
                else:
                        col=0
                '''
