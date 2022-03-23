### Resolución ejercicio 5
import math as math 
print("Ingrese las coordenadas de ambos puntos en la Tierra")
t1=int(input("Ingrese la laitud del primero punto en la Tierra: "))*math.pi/180
g1=int(input("Ingrese la longitud del primero punto en la Tierra: "))*math.pi/180
t2=int(input("Ingrese la laitud del segundo punto en la Tierra: "))*math.pi/180
g2=int(input("Ingrese la longitud del segundo punto en la Tierra: "))*math.pi/180

distancia=6371.01*math.acos(math.sin(t1)*math.sin(t2)+math.cos(t1)*math.cos(t2)*math.cos(g1-g2))
print("La distancia entre ambos puntos es: ",distancia, "Km")
