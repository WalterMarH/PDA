#Tarea Clase 0-100 divisibles entre 5
#Tradicional
for i in range(101): 
    if i%5==0:
        print(i)
#Comprimida
print([a for a in range(1,100) if a%5==0])

