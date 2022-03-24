numrs=4
num=[0]*numrs
for i in range(numrs):
    num[i] = int(input())
 
for i in range(numrs-1):
    for j in range(i+1,numrs):
        if(num[i] > num[j]):
            cambio = num[i]
            num[i] = num[j]
            num[j] = cambio
 
for i in range(numrs):
    print(num[i])