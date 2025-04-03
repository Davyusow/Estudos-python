#!/usr/bin/env python3

n = list()

for i in range(0,5):    
    n.append(int(input(f'Insira o {i+1}° valor: ')))

for i in range(0,len(n)-1): #insertion sort
    if(n[i]>n[i+1]):
        temp = n[i+1]
        n[i+1] = n[i]
        n[i] = temp
        j = i-1
        while(j>=0):
            if(temp<n[j]):
                n[j+1] = n[j]
                n[j] = temp
            else:
                break
            j-=1
print(n)
