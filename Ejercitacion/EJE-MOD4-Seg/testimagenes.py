import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


#img = mpimg.imread('leona.jpg')
#print('2')
# print(img)

#imgplot = plt.imshow(img)
#mpimg.imsave('juan2.jpg',img)
#plt.show()
canales=3
columnas=100
filas=100
imagen=np.zeros((filas,columnas,canales),int)
print(imagen[2,3,0])
for c in range(canales):
    for n in range(columnas):
        for m in range(filas):
            imagen[m,n,c]=200
imgplot = plt.imshow(imagen)
plt.show()

print(imagen[2,3,0])


