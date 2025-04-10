# importamos la libreria pygame
import pygame
import random

# inicializamos los modulos de pygame
pygame.init()

# Establecer titulo de la ventana
pygame.display.set_caption("surface")

# Establecemos las ordenes de la ventana 
ventana = pygame.display.set_mode((400,400))

# definidos un color
azul = (0, 0, 256)
verde = (0, 0, 256)
rojo = (0, 0, 256)

# crear una superficie
azul_superficie = pygame.Surface((400,400))
verde_superficie = pygame.Surface((400,400))
rojo_superficie = pygame.Surface((400,400))

# rellenamos la superficie de azul 
azul_superficie.fill(azul)
verde_superficie.fill(verde)
rojo_superficie.fill(rojo)

# inserto la superficie de la ventana 
ventana.blit(rojo_superficie, (0,0))
ventana.blit(azul_superficie, (0,0))
ventana.blit(verde_superficie, (0,0))

# actualiza la visualizacion de la ventana
pygame.display.flip()

# bucle del juego
while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT :
            break
