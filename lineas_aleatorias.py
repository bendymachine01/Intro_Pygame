import pygame
import sys
import random

coloraleatorio1 = (33,234,2)
coloraleatorio2 = (100,111,175)
blanco = (225,225,225)

pygame.init()

ventana = pygame.display.set_mode((600, 600))
pygame.display.set_caption("líneas aleatorias")

clock = pygame.time.Clock()

rect_x = 60
rect_y = 126
rect_w = 500
rect_h = 450

while 1:
    clock.tick(10)
    ventana.fill(coloraleatorio2)

    fuente_arial = pygame.font.SysFont("Arial", 35, 1, 1)
    texto = fuente_arial.render("Colegio San Jose de Guanenta", 1, coloraleatorio1)
    ventana.blit(texto, (60, 50))
    texto = fuente_arial.render("ESP.SISTEMAS", 1, coloraleatorio1)
    ventana.blit(texto, (70, 90))
    texto = fuente_arial.render("Harold Martinez", 1, coloraleatorio1)
    ventana.blit(texto, (70, 573))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.draw.rect(ventana, blanco, ((rect_x, rect_y), (rect_w, rect_h)), 1)

    for _ in range(100):
        orientacion = random.choice(["horizontal", "vertical"])
        color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

        if orientacion == "horizontal":
            y = random.randint(rect_y, rect_y + rect_h)
            x1 = random.randint(rect_x, rect_x + rect_w)
            x2 = random.randint(rect_x, rect_x + rect_w)
            pygame.draw.line(ventana, color, (x1, y), (x2, y), 1)
        else:
            x = random.randint(rect_x, rect_x + rect_w)
            y1 = random.randint(rect_y, rect_y + rect_h)
            y2 = random.randint(rect_y, rect_y + rect_h)
            pygame.draw.line(ventana, color, (x, y1), (x, y2), 1)

    pygame.display.flip()

