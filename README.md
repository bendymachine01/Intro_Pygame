# Estructura de un juego en pygame
 
 ##  Inicializacion 

 - comoen todo programa de python, se debe importar los modulos o librerias a utilizar 
 `import pygame`

 - inicializar pygame usado la fucion init(). Inicializa todos los modulos e pygame importados.
 `pygame.init()`

 ## visualizacion de la ventana

`ventana = pygame.display.set_mode((600,400))`

- set_mode() es la funcion encargada de difinir el tamaño  de la ventana. En el ejemplo, se sta definiendo una ventana de 600 px de ancho, por 400 px de alto.

`pygame.display.set_caption("Mi ventana")`

- .set_caption() es la funcion que añade un titulo en en la ventana

### Funcion set_model 
`set_model(size = (0.0).flags = 0. dsplay = 0`
- size = (000.400) : defineel tamaño de la pantalla
-  flags = define uno o mas conportamientos para la ventana.
    valores:
    - pygame.Fullscreen 
    - pygame.resizable
    Ejemplo:
    - flags = pygame.FULLSCREEN pygame
    Resizable: pantalla completa.
    dimenciones midificables 
## Bucle del juego - game loop
- blucle infinito del juego que se interrumpira al cumplir ciertos criterios 
- Reloj interno del juego 
- En cada iteracon de bucle del juego podemos moever un personje, o tener en cuenta que un objeto  alcanzado a otro o que a cruzado la linea de llegado quiere decier que la partida ha terminado 

- cada iteracion es una portunidad para actualizar todos los datos reacionados con el estado actual de la partida 

- en cada iteracion se realizan las siguientes tareas 
    1. comprobar que no alcancen las cndicones de parada, en cuyo caso se interrumpe el bucle.
    2. actualizar los recursos necesarios para la iteracion actual.
    3. obtener las entradas de sistemas, o de interaccion del jugador 
    4. obtener todas las identidades  que caracterizan el juego 
    5. refrescar la pantalla

    # Estructura de un juego en pygame 
    ## superficies pygame 
    - superficie:
    - elmento geometrico 
    - linea, poligono, imagen,texto que se muestra en la pantalla
    - las superficies se crean de difernte manera dependiendo del tipo:
    - imagen : image.load()
    - texto : font.reader()
    -superficie genrica : pygame .surface()
    - ventana de juego : pygame .display.set_mode()
    