import pygame
import sys
import random

pygame.init()

ventana = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Tren bajo la lluvia")

clock = pygame.time.Clock()

# Colores
verde_texto = (33, 234, 2)
fondo = (100, 111, 175)
blanco = (255, 255, 255)
gris = (160, 160, 160)
gris_oscuro = (90, 90, 90)
chimenea = (128, 0, 128)
techo = (0, 128, 128)
rueda = (25, 25, 112)
negro = (0, 0, 0)
amarillo = (255, 255, 0)
rojo = (255, 69, 0)
azul_claro = (180, 220, 255)

# Área del rectángulo (zona de lluvia)
rect_x, rect_y, rect_w, rect_h = 60, 126, 500, 450

# Generar gotas dentro del rectángulo
lluvia = []
for _ in range(100):
    x = random.randint(rect_x + 5, rect_x + rect_w - 5)
    y = random.randint(rect_y, rect_y + rect_h)
    velocidad = random.randint(4, 8)
    longitud = random.randint(7, 12)
    lluvia.append([x, y, velocidad, longitud])

while True:
    clock.tick(30)
    ventana.fill(fondo)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Dibujar rectángulo (marco) de lluvia
    pygame.draw.rect(ventana, blanco, ((rect_x, rect_y), (rect_w, rect_h)), 2)

    # Dibujar lluvia solo dentro del rectángulo
    for gota in lluvia:
        x, y, vel, largo = gota
        if rect_y <= y <= rect_y + rect_h:
            pygame.draw.line(ventana, azul_claro, (x, y), (x, y + largo), 1)
        gota[1] += vel
        if gota[1] > rect_y + rect_h:
            gota[0] = random.randint(rect_x + 5, rect_x + rect_w - 5)
            gota[1] = rect_y - 10

    # Texto
    fuente = pygame.font.SysFont("Arial", 35, 1, 1)
    ventana.blit(fuente.render("Colegio San Jose de Guanenta", True, verde_texto), (60, 50))
    ventana.blit(fuente.render("ESP.SISTEMAS", True, verde_texto), (70, 90))
    ventana.blit(fuente.render("Harold Martinez", True, verde_texto), (70, 573))

    # Posición tren
    tren_x = 100
    tren_y = 380

    # Tren
    pygame.draw.rect(ventana, gris, (tren_x, tren_y, 280, 80))  # cuerpo
    pygame.draw.rect(ventana, blanco, (tren_x + 180, tren_y - 80, 100, 80))  # cabina
    pygame.draw.rect(ventana, techo, (tren_x + 160, tren_y - 110, 140, 40))  # techo
    pygame.draw.rect(ventana, gris_oscuro, (tren_x + 185, tren_y - 50, 90, 30))  # base cabina
    pygame.draw.rect(ventana, blanco, (tren_x + 20, tren_y - 75, 50, 15))  # tapa chimenea
    pygame.draw.rect(ventana, chimenea, (tren_x + 35, tren_y - 60, 20, 40))  # chimenea
    pygame.draw.rect(ventana, blanco, (tren_x - 20, tren_y + 5, 15, 60))  # frente

    # Ruedas
    pygame.draw.circle(ventana, rueda, (tren_x + 30, tren_y + 80), 30)
    pygame.draw.circle(ventana, rueda, (tren_x + 120, tren_y + 80), 30)
    pygame.draw.circle(ventana, rueda, (tren_x + 210, tren_y + 80), 30)

    # Emoji humanoide
    cara_x = tren_x + 230
    cara_y = tren_y - 40
    pygame.draw.circle(ventana, amarillo, (cara_x, cara_y), 25)  # cabeza
    pygame.draw.ellipse(ventana, blanco, (cara_x - 15, cara_y - 12, 10, 16))  # ojo izq
    pygame.draw.ellipse(ventana, blanco, (cara_x + 5, cara_y - 12, 10, 16))   # ojo der
    pygame.draw.circle(ventana, negro, (cara_x - 10, cara_y - 3), 3)          # pupila izq
    pygame.draw.circle(ventana, negro, (cara_x + 10, cara_y - 3), 3)          # pupila der
    pygame.draw.arc(ventana, rojo, (cara_x - 10, cara_y + 5, 20, 10), 3.14, 0, 2)  # sonrisa
    pygame.draw.line(ventana, negro, (cara_x - 14, cara_y - 17), (cara_x - 5, cara_y - 20), 2)  # ceja izq
    pygame.draw.line(ventana, negro, (cara_x + 5, cara_y - 20), (cara_x + 14, cara_y - 17), 2)  # ceja der

    pygame.display.flip()
