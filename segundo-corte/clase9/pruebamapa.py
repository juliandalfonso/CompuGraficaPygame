import pygame
import Repo as rep

def cut(img, columnasx, filas, an_c,al_c):
        imagenes = []
        for i in range(columnasx):
                imagenes.append([])

        for i in range(columnasx):
                for j in range(filas):
                        cuadro = img.subsurface(i*an_c, j*al_c, an_c, al_c)
                        imagenes[i].append(cuadro)

        return imagenes


if __name__ == '__main__':
    pygame.init()
    reloj=pygame.time.Clock()
    pantalla=pygame.display.set_mode([rep.ANCHOPANTALLA,rep.ALTOPANTALLA])
    img = pygame.image.load ('terrenogen.png')
    # ESTO DEBE HACER LA FUNCION
    m = cut(img,32,12,32,32)
    pantalla.blit(m,[10,10])

    #Codigo

    pygame.display.flip()
    fin = False
    while not fin:
        #reloj.tick(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True


        pantalla.fill(negro)
        pygame.display.flip()
        reloj.tick(10)
