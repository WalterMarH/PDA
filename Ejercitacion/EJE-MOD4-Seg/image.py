"""Clase Image para el ejercicio de la Ejercitación Módulo 4 - Segunda Parte"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from utils2 import crearMatrix

class Image():
    """Documentación de Image"""

    def __init__(self, dimensiones:tuple = None, filename:str = ""):
        """Crea una matriz 2D a partir de image o de filename"""

        if dimensiones:
            self.image = crearMatrix(dimensiones)
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
        amostrar=plt.imshow(self.image.astype(np.uint8))
        plt.show()

        

    def size(self):
        """Retorna una tupla de la forma (filas, columnas)"""


        return self.fil , self.col

    def saveImage(self, filename:str):
        """Guarda la imágen en un archivo jpg"""
        mpimg.imsave(filename,self.image)
        
# canales=3
# columnas=1920
# filas=1080

# imagen2=Image((filas,columnas,canales))
# #imagen=Image(filename='bote.jpg')
# brillosa=ajustarBrillo(imagen2.image,0.5)
# imagen2.showImage()
# amostrar=plt.imshow(brillosa)

# #imagen.showImage()
# print(imagen2.size())
# print(imagen2.col)
# print(imagen2.fil)
# #imagen.saveImage('bote2.jpg')


