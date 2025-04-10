import pygame, sys
pygame.init()

ventana = pygame.display.set_mode((400, 400))
pygame.display.set_caption("cuadro centrado y otros en las orillas")
clock = pygame.time.Clock()

tam = 50
cx, cy = 160, 160
colores = [(255, 0, 0), (0, 255, 0), (255, 255, 0), (0, 255, 255), (255, 0, 255)]
colores_bordes = [(255, 255, 0), (0, 255, 0), (0, 255, 255), (255, 0, 255)]

ix, dx = 0, 350
iy, dy = 0, 350
vx1, vx2 = 3, -3
vy1, vy2 = 3, -3

i = 0
c = 0

while True:
    clock.tick(60)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ix += vx1
    dx += vx2
    iy += vy1
    dy += vy2

    if ix <= 0 or ix >= 350: vx1 *= -1
    if dx <= 0 or dx >= 350: vx2 *= -1
    if iy <= 0 or iy >= 350: vy1 *= -1
    if dy <= 0 or dy >= 350: vy2 *= -1

    ventana.fill((0, 0, 225))

    pygame.draw.rect(ventana, colores_bordes[0], (ix, 0, tam, tam))
    pygame.draw.rect(ventana, colores_bordes[1], (dx, 350, tam, tam))
    pygame.draw.rect(ventana, colores_bordes[2], (0, iy, tam, tam))
    pygame.draw.rect(ventana, colores_bordes[3], (350, dy, tam, tam))

    c += 1
    if c >= 10:
        c = 0
        i = (i + 1) % len(colores)

    pygame.draw.rect(ventana, colores[i], (cx, cy, 80, 80))
    pygame.display.flip()


