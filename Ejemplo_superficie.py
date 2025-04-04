# Importamos la librería pygame
import pygame

# Inicializamos los módulos de pygame
pygame.init()

# Establecer título a la pantalla
pygame.display.set_caption("Bandera de Colombia")

# Establecemos las dimensiones de la ventana
ANCHO = 400
ALTO = 240
ventana = pygame.display.set_mode((ANCHO, ALTO))

# Definimos los colores
AMARILLO = (255, 223, 0)  # Color amarillo
AZUL = (0, 0, 255)        # Color azul
ROJO = (255, 0, 0)        # Color rojo

# Dibujar la bandera
ventana.fill(AMARILLO)  # Franja superior amarilla (mitad superior)
pygame.draw.rect(ventana, AZUL, (0, ALTO // 2, ANCHO, ALTO // 4))  # Franja azul (1/4 parte inferior)
pygame.draw.rect(ventana, ROJO, (0, (ALTO // 4) * 3, ANCHO, ALTO // 4))  # Franja roja (último 1/4)

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

