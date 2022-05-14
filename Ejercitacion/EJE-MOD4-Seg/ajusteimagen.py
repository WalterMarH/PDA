from image import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from utils2 import crearMatrix



canales=3
columnas=1920
filas=1080

def ajustarBrillo(imagene, ajuste):
    """Doc..."""
    abrillar=imagene.image[::]
    for rgb in range(3):
        for n in range(imagene.col):
            for m in range(imagene.fil):
                abrillar[m,n,rgb]=int(abrillar[m,n,rgb]*ajuste)
    return abrillar

#imagen2=Image((filas,columnas,canales))
imagen=Image(filename='bote.jpg')
brillosa2=ajustarBrillo(imagen,1.5)
#amostrar=plt.imshow(brillosa2)

imagen.showImage()





def getHistograma(image):
    """Doc..."""
    pass

def getChannels(image):
    """Doc..."""
    pass

def ajustarContraste(image, alfa):
    """Doc..."""
    pass

def ajustarGamma(image, gamma):
    """Doc..."""
    pass

def aplicarKernel(image, kernel):
    """Doc..."""
    pass

def main():
    #Mostrar su implementación aquí
    pass

if __name__ == '__main__':
    main()