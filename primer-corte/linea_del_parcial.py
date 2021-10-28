import pygame
import Repo as rep


if __name__ == '__main__':
    pygame.init()
    reloj=pygame.time.Clock()
    pantalla=pygame.display.set_mode([rep.AnchoPantalla,rep.AltoPantalla])
    #Codigo
    lista_puntos=[]
    ls=[]
    n=0
    an=3
    rotar=False

    fin = False
    while not fin:
        #reloj.tick(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                psp = event.pos
                if (len(lista_puntos)<2):
                    lista_puntos.append(list(psp))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if rotar:
                        if n==0:
                            x1=rep.PantallaACartesiano(lista_puntos[0])
                            x2=rep.PantallaACartesiano(lista_puntos[1])
                            ls.append(x1)
                            ls.append(x2)
                            n+=1
                        else:
                            aux=[]
                            x=rep.Rotacion_Horaria(ls[0],an)
                            y=rep.Rotacion_Horaria(ls[1],an)
                            aux.append(rep.CartesianoApantalla(x))
                            aux.append(rep.CartesianoApantalla(y))
                            an+=20
                            print aux
                            pantalla.fill(rep.NEGRO)
                            pygame.draw.polygon(pantalla,rep.AZUL,aux,1)
                            pygame.display.flip()





        rep.plano_cartesiano(pantalla,rep.YELLOW)
        if (len(lista_puntos)>=2):
            pygame.draw.polygon(pantalla,rep.VERDE,lista_puntos,1)
            rotar=True
        pygame.display.flip()
