############################################################
#           PROYECTO RASTERIZADOR
#       Graficación por Computadora
#
#       Héctor Andrey Hernández Alonso
#       Benjamin Ulises Camacho    
#############################################################
import sys, pygame,os



def obtenCoordenada(cuadro,x1, j, x2, distanciaX, distanciaY ):
    i = x1
    while i < x2:
        cuadro.append([i,j,i+distanciaX,j+distanciaY])
        i = i + distanciaX



def obtenTam():
    n = int(input("Tam de la matriz: "))
    return n

def generaCuadricula(N, x1,y1,x2,y2,screen, cuadro):
    distanciaX = int((x2 - x1)/N)
    distanciaY = int((y2 - y1)/N)
    i = x1
    j = y1

    while i <= x2 or j <= y2:
        color = (40,210,250)
        starPosX = (i,y1)
        endPosX  = (i,y2)

        starPosY = (x1,j)
        endPosY  = (x2,j)
        obtenCoordenada(cuadro,x1, j, x2, distanciaX, distanciaY )
        width = 1
        pygame.draw.line(screen, color, starPosX, endPosX, width)
        pygame.draw.line(screen, color, starPosY, endPosY, width)

        i  = i + distanciaX
        j = j + distanciaY

def rellenaFigura(cuadro,screen):
    colorB = 0
    colorA = 0
    black = (0,0,0,0)
    color = (0,0,0)
    for  c in cuadro:
        i = c[1]
        while i <  c[2]:
            j = c[0]
            while j < c[3]:
                actual = screen.get_at((int(c[0]+1),int(c[1]+1)))
                #print("valor de actual",  actual)
                if actual != black : 
                    colorB = colorB + 1
                    color = actual
                else:
                    colorA = colorA + 1
                j = j + 1
            i = i + 1
        y = c[1]
        if(colorB > colorA):
            while y < c[3]:
                x = c[0]
                while x < c[2]:
                    screen.set_at((x,y),color) 
                    x = x + 1
                y = y + 1
        
    print("fin")
#####################################################################################################


# Inicializamos pygame
pygame.init()

# Tamaño de ventana
size = 800, 600
screen = pygame.display.set_mode(size)
# Titulo de la ventana
pygame.display.set_caption("Rasterizador")
print("Archivos en el directorio")
print(os.listdir())
print("Dame el nombre del archivo ")
nomArchivo=input()
nomArchivo=nomArchivo+'.png'
imagen = pygame.image.load(nomArchivo)
tamImagen = imagen.convert()
screen.blit(imagen,(100,100))

TextButton= pygame.draw.rect(screen,(12,100,0), (50, 10, 200,20),2)

x1 = 100
y1 = 100
x2 = x1 + tamImagen.get_width()
y2 = y1 + tamImagen.get_height()

print("El ancho es ", x2)
print("El alto es", y2)

cuadro = [] #lista

r = obtenTam()
generaCuadricula(r,x1,y1,x2,y2,screen, cuadro)
rellenaFigura(cuadro,screen)
pygame.display.update()

# Comenzamos el bucle del juego
run=True
while run:
    # Capturamos los eventos que se han producido
    for event in pygame.event.get():
        # Si el evento es salir de la ventana, terminamos
        if event.type == pygame.QUIT: run = False

pygame.quit()



