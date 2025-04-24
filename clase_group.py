import pygame
import sys

pygame.init()

# Configuración de la pantalla
ANCHO, ALTO = 400, 300
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ejemplo con Sprite")

# Colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)

# Grupo de sprites
all_sprites_group = pygame.sprite.Group()

# Clase Sprite
class MySprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites_group)
        self.image = pygame.Surface([20, 20])
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Crear el sprite e incluirlo en el grupo
my_sprite = MySprite(100, 100)

# Bucle principal
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ventana.fill(BLANCO)
    all_sprites_group.draw(ventana)
    pygame.display.flip()
    clock.tick(60)
