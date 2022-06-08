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
ajuste=140
imagen=np.zeros((filas,columnas,canales),int)
arraybrillo=np.full((filas,columnas,canales), ajuste)
array=np.histogram(arraybrillo)
print(array)






