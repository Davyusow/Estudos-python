#!/usr/bin/env python3

tam = int(input('Digite quantos números da sequência de fibonacci deseja ver: '))
n1 = 1; n2 = 0;n3 = 0 #o n1 é o termo atual, enquanto o n2 é o termo uma casa atrás e o n3 de duas casas atrás
i=0
while(i<tam):
    if(i==tam-1):
        print('{} '.format(n3))
    else:
        print('{} '.format(n3),end=' → ')
    n2 = n1
    n1 = n3
    n3 = n1+n2
    i+=1
