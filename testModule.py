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

def main():
    print("Estamos haciendo pruebas")
    print(suma(1,2,3))
    print(isPar(9))
    print("Todo esto NO debería verse cuando importo mi módulo")
    print("Sólo deberíamos verlo cuando ejecutamos el script")

if __name__ == "__main__":
    main()