import numpy as np

arra=np.ones((6,7,8))
array=np.cumsum(arra)
array2=np.reshape(array,(6,7,8))


def test(a):
    a=a*2
    return a

vfunc=np.vectorize(test)
nueva=vfunc(array2)
print(nueva)
