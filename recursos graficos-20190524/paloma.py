import pygame
import Repo as rep
'''
pasos para adicionar objtos
1 crear la Clase
2 crear el grupo
3crear el objeto e instanciar la clase
4 dibujarlo
'''

class Jugador(pygame.sprite.Sprite):
    '''
    Clase Jugador
    '''
    def __init__(self,p,cl=rep.BLANCO):
    #def __init__(self,id,p,cl=rep.BLANCO):

        pygame.sprite.Sprite.__init__(self)
        #self.id=id
        self.image=pygame.Surface([40,50])
        self.image.fill(cl)
        self.rect=self.image.get_rect()
        self.rect.x=p[0]
        self.rect.y=p[1]
        self.velx=0
        self.vely=0
        self.bombas=0
        self.vidas=3

    def update(self):    #le permite al pobjeto actualizar su estado
        self.rect.x +=self.velx
        self.rect.y +=self.vely





if __name__ == '__main__':
    pygame.init()
    reloj=pygame.time.Clock()
    Pantalla=pygame.display.set_mode([rep.ANCHOPANTALLA,rep.ALTOPANTALLA])

    #Codigo

    pygame.display.flip()
    fin = False
    while not fin:
        #reloj.tick(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
