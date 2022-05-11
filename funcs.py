"""
Conjunto de funciones de ejemplo
"""

def suma(*keyArgs):
    sum = 0
    for arg in keyArgs:
        sum += arg

    return sum


def isPar(num):
   return True if num%2==0 else False

print(suma(2,34))
print("Hola mundo")