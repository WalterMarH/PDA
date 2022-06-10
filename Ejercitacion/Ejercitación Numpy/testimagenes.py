import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


img = mpimg.imread('starship.jpg')
print(img.shape)
print(img.shape[0]/2)
print(img.shape[1]/2)
cuad1=img[0:175,0:295, : ]
cuad2=img[175:350,0:295, : ]
cuad3=img[0:175,295:590, : ]
cuad4=img[175:350,295:590, : ]
imgplot = plt.imshow(img)
plt.show()
imgplot = plt.imshow(cuad1)
plt.show()
imgplot = plt.imshow(cuad2)
plt.show()
imgplot = plt.imshow(cuad3)
plt.show()
imgplot = plt.imshow(cuad4)
plt.show()


#mpimg.imsave('juan2.jpg',img)
#plt.show()
# canales=3
# columnas=100
# filas=100
# ajuste=140
# imagen=np.zeros((filas,columnas,canales),int)
# arraybrillo=np.full((filas,columnas,canales), ajuste)
# array=np.histogram(arraybrillo)
# print(array)






