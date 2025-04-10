import pygame 
import sys

rojo = (255, 0, 0)
azul = (0, 0, 225)

pygame.init()

ventana = pygame.display.set_mode((400, 400))
pygame.display.set_caption("el cuadrado que rebota")
clock = pygame.time.Clock()

ancho_ventana = 400
ancho_cuadro = 80

xx = (ancho_ventana - ancho_cuadro) // 2
movimiento = 3

while True:
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ventana.fill(azul)

    xx += movimiento

    if xx >= ancho_ventana - ancho_cuadro:
        xx = ancho_ventana - ancho_cuadro
        movimiento = -3
    elif xx <= 0:
        xx = 0
        movimiento = 3 
    
    pygame.draw.rect(ventana, rojo, (xx, 200, 80, 80))
    pygame.display.flip()



