# Importamos la librería pygame
import pygame

# Inicializamos los módulos de pygame
pygame.init()

# Establecer título a la pantalla
pygame.display.set_caption("Bandera de Colombia")

# Establecemos las dimensiones de la ventana
ANCHO = 400
ALTO = 400
ventana = pygame.display.set_mode((ANCHO, ALTO))

# Definimos los colores
AMARILLO = (255, 223, 0) 
AZUL = (0, 0, 255)       
ROJO = (255, 0, 0)     

# Dibujar la bandera
ventana.fill(AMARILLO) 
pygame.draw.rect(ventana, AZUL, (0, ALTO // 2, ANCHO, ALTO // 4))  
pygame.draw.rect(ventana, ROJO, (0, (ALTO // 4) * 3, ANCHO, ALTO // 4))  
# Actualizar la pantalla
pygame.display.update()

# Bucle de juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Salir del bucle

# Cerramos pygame
pygame.quit()

