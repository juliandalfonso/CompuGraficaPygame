import pygame

ancho = 1200
alto  = 600

blanco = [255,255,255]
verde = [0,255,0]
negro = [0,0,0]

"""def coger_radio(list_):
    x = 0
    y = 0
    for pt in list_:
        if (pt[0]>pt[0]+30 and pt[0]<pt[0]-30 and pt[1]<pt[1]-30 and pt[1]>pt[1]+30):
            x = pt[0]
            y = pt[1]

    return x,y
"""





if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ancho,alto])
    lista_puntos = []
    agrandar = False
    fin = False

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                psp = event.pos
                if (len(lista_puntos)<3):
                    lista_puntos.append(list(psp))

                if agrandar:
                    """
                    x,y = coger_radio(lista_puntos)
                    lista_ayuda = []
                    lista_ayuda.append(x)
                    lista_ayuda.append(y)"""

                    #lista_puntos.append(lista_ayuda)


        pantalla.fill(negro)
        if (len(lista_puntos)>=3):
            pygame.draw.polygon(pantalla,verde,lista_puntos,1)
            agrandar = True









        pygame.display.flip()
