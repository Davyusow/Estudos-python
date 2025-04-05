#!/usr/bin/env python3
def contador(*num):
    #print(num) #retorna uma tupla
    tam = len(num)
    print(f'Recebi os valóre {num} e ao todo são {tam} números')

contador(1,5,8)
contador(2,5)
contador(9,2,5,1)
