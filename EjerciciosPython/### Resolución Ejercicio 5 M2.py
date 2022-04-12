### Resolución Ejercicio 5
a=0
while a!="p":
    a=int(input("Ingrese el radio del circulo en cm: "))
    area=a**2*3.141592
    print("Área es: ",area,"m2")
    a=input("Si quieres no seguir calculando áreas, apreta INTRO ")
    try:
        int(a)
    except:
        a="p"



### TODO