import pygame
import time
import random

# Inicializar Pygame
pygame.init()

# Colores
Negro = (0, 0, 0)
Blanco = (255, 255, 255)
Rojo = (213, 50, 80)
Verde = (0, 255, 0)
Azul = (50, 153, 213)

# Tamaño de la ventana
ancho_ventana = 600
alto_ventana = 400

# Crear la ventana
ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption('Juego de Serpiente')

# Configuración de la serpiente
tamaño_celda = 10
velocidad_serpiente = 15

# Reloj para la velocidad del juego
reloj = pygame.time.Clock()

# Fuentes
fuente = pygame.font.SysFont("bahnschrift", 25)
fuente_puntuacion = pygame.font.SysFont("comicsansms", 35)

def mostrar_puntuacion(puntuacion):
    texto = fuente_puntuacion.render("Puntuación: " + str(puntuacion), True, Blanco)
    ventana.blit(texto, [0, 0])

def gameLoop():
    game_over = False
    game_close = False

    x1 = ancho_ventana / 2
    y1 = alto_ventana / 2

    x1_cambio = 0
    y1_cambio = 0

    serpiente = []
    longitud_serpiente = 1

    comida_x = round(random.randrange(0, ancho_ventana - tamaño_celda) / 10.0) * 10.0
    comida_y = round(random.randrange(0, alto_ventana - tamaño_celda) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            ventana.fill(Negro)
            mensaje = fuente.render("Perdiste! Presiona C para jugar de nuevo o Q para salir", True, Rojo)
            ventana.blit(mensaje, [ancho_ventana / 6, alto_ventana / 3])
            mostrar_puntuacion(longitud_serpiente - 1)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if evento.key == pygame.K_c:
                        gameLoop()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x1_cambio = -tamaño_celda
                    y1_cambio = 0
                elif evento.key == pygame.K_RIGHT:
                    x1_cambio = tamaño_celda
                    y1_cambio = 0
                elif evento.key == pygame.K_UP:
                    y1_cambio = -tamaño_celda
                    x1_cambio = 0
                elif evento.key == pygame.K_DOWN:
                    y1_cambio = tamaño_celda
                    x1_cambio = 0

        if x1 >= ancho_ventana or x1 < 0 or y1 >= alto_ventana or y1 < 0:
            game_close = True

        x1 += x1_cambio
        y1 += y1_cambio
        ventana.fill(Azul)
        pygame.draw.rect(ventana, Verde, [comida_x, comida_y, tamaño_celda, tamaño_celda])
        serpiente_cabeza = []
        serpiente_cabeza.append(x1)
        serpiente_cabeza.append(y1)
        serpiente.append(serpiente_cabeza)

        if len(serpiente) > longitud_serpiente:
            del serpiente[0]

        for x in serpiente[:-1]:
            if x == serpiente_cabeza:
                game_close = True

        for segmento in serpiente:
            pygame.draw.rect(ventana, Blanco, [segmento[0], segmento[1], tamaño_celda, tamaño_celda])

        mostrar_puntuacion(longitud_serpiente - 1)

        pygame.display.update()

        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, ancho_ventana - tamaño_celda) / 10.0) * 10.0
            comida_y = round(random.randrange(0, alto_ventana - tamaño_celda) / 10.0) * 10.0
            longitud_serpiente += 1

        reloj.tick(velocidad_serpiente)

    pygame.quit()

gameLoop()