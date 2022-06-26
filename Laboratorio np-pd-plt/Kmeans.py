#Kmeans
from Picos import peakdet
import numpy as np 
import matplotlib.pyplot as plt
data = np.load('datos/ecg/100_10min_filtered.npy')
data2=data[0:10000]
data=data[0:10000]
def mediaMovil(array, n) :
    acum = np.cumsum(array) #genera array con sumas acumuladas
    acum[n:] = acum[n:] - acum[:-n] #a los valores a partir de indice n, les asigna el valor de la diferencia entre los valores a partir de n y hasta -n (-n siendo empezando desde atras, si tiene 40 indices y ene es 5, seria contando hacia atras desde 45)
    return acum[n-1:] / n #divido entre n los valores a partir de n-1, y los retorno.
data2=mediaMovil(data2,15)
fig, ax= plt.subplots(figsize=(18,2))
picos=peakdet(data2,40)
ax.plot(np.arange(len(data)),data)
indices=picos[0][:,0]
indicesint=[]
for i in indices:
    indicesint.append(int(i))
print(indicesint)
ax.plot(picos[0][:,0],data[indicesint],"*")
#ax.plot(picos[0][:,0]+9,picos[0][:,1],"*")
plt.show()

print(data2.shape)
print(data.shape)
