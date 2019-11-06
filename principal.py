############################################################
#           PROYECTO RASTERIZADOR
#       Graficación por Computadora
#
#       Héctor Andrey Hernández Alonso
#       Benjamin Ulises Camacho    
#############################################################

import sys, pygame
# Inicializamos pygame
pygame.init()

# Tamaño de ventana
size = 800, 600
screen = pygame.display.set_mode(size)
# Titulo de la ventana
pygame.display.set_caption("Rasterizador")

imagen = pygame.image.load("hongo.png")
tamImagen = imagen.convert()
screen.blit(imagen,(100,100))

TextButton= pygame.draw.rect(screen,(12,100,0), (50, 10, 200,20),2)

x1 = 100
y1 = 10
x2 = x1 + tamImagen.get_width()
y2 = y1 + tamImagen.get_height()

print("El ancho es ", x2)
print("El alto es", y2)


n = int(input("Tam de la matriz: "))
pygame.display.update()

# Comenzamos el bucle del juego
run=True
while run:
    # Capturamos los eventos que se han producido
    for event in pygame.event.get():
        # Si el evento es salir de la ventana, terminamos
        if event.type == pygame.QUIT: run = False

pygame.quit()

