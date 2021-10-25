#Modulos
import pygame, sys, math
from pygame.locals import *
ANCHO=400
ALTO=600
lista=[]
a=0
b=0
c=1
d=1




def Cut(F,C,Tx,Ty,img,tam):
    """F: Fila a cortar
		C: Columna a cortar
		Tx: Tamanio de columnas de imagen
		Ty: Tamanio de filas de imagen
		img: Imagen a cortar
		tam:tamanio de recorte 32 x 32 o 64 x 64
    """
    Mat=[]
    for h in range (Tx):
        ls = []
        for i in range (Ty):
            cuadro = img.subsurface(tam*h,tam*i,tam,tam)
            ls.append(cuadro)
        Mat.append(ls)
    cuadro = Mat[F][C]
    print cuadro
    return cuadro


if __name__ == "__main__":

  pygame.init()
  pantalla = pygame.display.set_mode((ANCHO, ALTO))
  img = pygame.image.load('terrenogen.png')
  imagen_cout=Cut(17,3,32,12,img,32)
  '''envio la imagen (fil, col,num filasa, num col, cargo la imagen, tam pixels)'''
  pantalla.blit(imagen_cout,[10,10])
  pygame.display.flip()

  fin= False
  while not fin:
      for evento in pygame.event.get():
          if evento.type == QUIT:
              fin=True
