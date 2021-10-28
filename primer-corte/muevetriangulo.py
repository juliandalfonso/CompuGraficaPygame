import pygame
from Mirepositorio import*



if __name__ == '__main__':
    pygame.init()
    reloj = pygame.time.Clock()
    Pantalla = pygame.display.set_mode([Mirepositorio.ANCHOPANTALLA,Mirepositorio.ALTOPANTALLA])
    centro=[300,200]  #centro de la pantalla
    plano_cartesiano_centro(p,ROJO,centro)
    ls=[]

    # Codigo

    reloj = pygame.time.Clock()
    fin = False
    while not fin:
        # reloj.tick(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                ls.append(pos)
        if(len(ls) == 3):
            pygame.draw.polygon(pantalla, Mirepositorio.GREEN, ls, 1)
        pygame.display.flip()
