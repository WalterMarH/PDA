
from image import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from utils2 import crearMatrix
import copy


canales=3
columnas=1920
filas=1080

def ajustarBrillo(imagene, ajuste):
    """Doc..."""
    brilloajustado=copy.deepcopy(imagene)
    abrillar=brilloajustado.image[::]
    for rgb in range(3):
        for n in range(imagene.col):
            for m in range(imagene.fil):
                abrillar[m,n,rgb]=int(abrillar[m,n,rgb]*ajuste)
    #brilloajustado.showImage()
    return brilloajustado



def getHistograma(image):
    """Doc..."""
    pass

def getChannels(image):
    """Doc..."""
    pass

def ajustarContraste(image, alfa):
    """Ajusta el contraste de una imágen.
    
    Retorna una nueva imágen con las mismas dimensiones de la imágen original.
    """
    imagenProcesada=copy.deepcopy(image)

    for canal in range(3):
        for i in range(imagenProcesada.fil):
            for j in range(imagenProcesada.col):
                pixel = int(alfa*(imagenProcesada.image[i][j][canal]-128) + 128)
                if pixel < 0:
                    pixel = 0
                elif pixel > 255:
                    pixel = 255
                imagenProcesada.image[i][j][canal] = pixel
                
    return imagenProcesada

def ajustarGamma(image, gamma):
    """Doc..."""
    pass

def aplicarKernel(image, kernel):
    """Doc..."""
    contador=0
    imagenProcesada=copy.deepcopy(image)
    c=kernel[0][0]+kernel[0][1]+kernel[0][2]+kernel[1][0]+kernel[1][1]+kernel[1][2]+kernel[2][0]+kernel[2][1]+kernel[2][2]
    if c==0:
        c=1
    for canal in range(3):
        for i in range(1,imagenProcesada.fil-1):
            for j in range(1,imagenProcesada.col-1):
                # p00=(imagenProcesada.image[i-1,j-1,canal])*kernel[0][0]
                # p01=(imagenProcesada.image[i-1,j,canal])*kernel[0][1]
                # p02=(imagenProcesada.image[i-1,j+1,canal])*kernel[0][2]
                # p10=(imagenProcesada.image[i,j-1,canal])*kernel[1][0]
                # p11=(imagenProcesada.image[i,j,canal])*kernel[1][1]
                # p12=(imagenProcesada.image[i,j+1,canal])*kernel[1][2]
                # p20=(imagenProcesada.image[i+1,j-1,canal])*kernel[2][0]
                # p21=(imagenProcesada.image[i+1,j,canal])*kernel[2][1]
                # p22=(imagenProcesada.image[i+1,j+1,canal])*kernel[2][2]
                p00=(imagenProcesada.image[i-1,j-1,canal])*kernel[0][0]
                p01=(imagenProcesada.image[i-1,j,canal])*kernel[0][1]
                p02=(imagenProcesada.image[i-1,j+1,canal])*kernel[0][2]
                p10=(imagenProcesada.image[i,j-1,canal])*kernel[1][0]
                p11=(imagenProcesada.image[i,j,canal])*kernel[1][1]
                p12=(imagenProcesada.image[i,j+1,canal])*kernel[1][2]
                p20=(imagenProcesada.image[i+1,j-1,canal])*kernel[2][0]
                p21=(imagenProcesada.image[i+1,j,canal])*kernel[2][1]
                p22=(imagenProcesada.image[i+1,j+1,canal])*kernel[2][2]
                pixel = (p00+p01+p02+p10+p11+p12+p20+p21+p22)//c
                contador=contador+1
                if pixel < 0:
                    pixel = 0
                elif pixel > 255:
                    pixel = 255
                pixel=int(pixel)
                print(contador)
                imagenProcesada.image[i][j][canal] = pixel
    return imagenProcesada

def main():
    #Mostrar su implementación aquí
    #imagen2=Image((8,8,3))
    imagen=Image(filename='bote.jpg')
    #brillosa2=
    #brilloajustado=ajustarBrillo(imagen,1.5)
    #amostrar=plt.imshow(brillosa2)

    #brilloajustado.showImage()
    #contrastada=ajustarContraste(imagen,0.7)
    imagen.showImage()
    #contrastada.showImage()
    #kernel=[[0.0625,0.125,0.0625],[0.125,0.25,0.125],[0.0625,0.125,0.0625]] #blur
    kernel=[[0,-1,0],[-1,8,-1],[0,-1,0]] #sharpen
    #print(kernel[0][0]+kernel[0][1]+kernel[0][2]+kernel[1][0]+kernel[1][1]+kernel[1][2]+kernel[2][0]+kernel[2][1]+kernel[2][2])
    kerneleada=aplicarKernel(imagen,kernel)
    kerneleada.showImage()
    #print(kernel[2][2])
    pass

if __name__ == '__main__':
    
    main()


