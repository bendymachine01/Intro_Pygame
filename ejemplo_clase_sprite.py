import pygame
import sys
import random

pygame.init()

# Pantalla
ANCHO, ALTO = 600, 400
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Atrapa el Círculo")
fuente = pygame.font.SysFont("Arial", 24)

# Colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
NEGRO = (0, 0, 0)

# Jugador
jugador = pygame.Rect(275, 175, 50, 50)

# Objetivo
objetivo = pygame.Rect(random.randint(0, ANCHO-30), random.randint(0, ALTO-30), 30, 30)

puntos = 0
velocidad = 5
reloj = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jugador.x -= velocidad
    if teclas[pygame.K_RIGHT]:
        jugador.x += velocidad
    if teclas[pygame.K_UP]:
        jugador.y -= velocidad
    if teclas[pygame.K_DOWN]:
        jugador.y += velocidad

    # Colisiones y puntos
    if jugador.colliderect(objetivo):
        puntos += 1
        objetivo.x = random.randint(0, ANCHO - 30)
        objetivo.y = random.randint(0, ALTO - 30)

    # Dibujar
    ventana.fill(BLANCO)
    pygame.draw.rect(ventana, ROJO, jugador)
    pygame.draw.ellipse(ventana, VERDE, objetivo)

    texto = fuente.render(f"Puntos: {puntos}", True, NEGRO)
    ventana.blit(texto, (10, 10))

    pygame.display.flip()
    reloj.tick(60)
