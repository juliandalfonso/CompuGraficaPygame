import pygame
import Repo as rep


if __name__ == '__main__':

    pygame.init()
    reloj=pygame.time.Clock()
    pantalla=pygame.display.set_mode([rep.ANCHOPANTALLA,rep.ALTOPANTALLA])

    #Codigo

    reloj = pygame.time.Clock()
    pygame.display.flip()
    fin = False
    while not fin:
        #reloj.tick(5)
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                #pos = pygame.mouse.get_pos()
                posx = pos[0]
                posy = pos[1]

        pantalla.fill(rep.NEGRO)
        rep.plano_cartesiano_centro(pantalla,rep.VERDE,pos)
        pygame.display.flip()
