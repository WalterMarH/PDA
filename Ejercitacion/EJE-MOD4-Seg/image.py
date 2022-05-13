"""Clase Image para el ejercicio de la Ejercitación Módulo 4 - Segunda Parte"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

class Image():
    """Documentación de Image"""

    def __init__(self, image:"numpy.Array" = 'nada', filename:str = ""):
        """Crea una matriz 2D a partir de image o de filename"""

        if image!='nada':
            self.image = image
            self.fil =  self.image.shape[0]
            self.col = self.image.shape[1]
        elif filename:
            self.image = self.loadImage(filename)
            self.fil =  self.image.shape[0]
            self.col = self.image.shape[1]
        else:
            raise ValueError("No se ha dado una imágen ni un archivo")

    def loadImage(self, filename:str):
        """Cargamos imágen"""
        imge=mpimg.imread(filename)

        return imge

    def showImage(self):
        """Mostramos imágen"""
        amostrar=jota2=plt.imshow(self.image)
        plt.show()

        

    def size(self):
        """Retorna una tupla de la forma (filas, columnas)"""


        return self.fil , self.col

    def saveImage(self, filename:str):
        """Guarda la imágen en un archivo jpg"""
        mpimg.imsave(filename,self.image)
        
canales=3
columnas=100
filas=100
imagen2=np.zeros((filas,columnas,canales),int)
for c in range(canales):
    for n in range(columnas):
        for m in range(filas):
            imagen2[m,n,c]=200
imagen2=Image(image=imagen2)
imagen=Image(filename='bote.jpg')
imagen2.showImage()
imagen.showImage()
print(imagen.size())
print(imagen.col)
print(imagen.fil)
#imagen.saveImage('bote2.jpg')


