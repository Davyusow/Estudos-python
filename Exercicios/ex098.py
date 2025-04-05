#!/usr/bin/env python3
from time import sleep
def contagem(inicio,fim,passo):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if(passo == 0): passo = 1
    if(fim<inicio and passo >0): passo*=-1 ; fim-=2
    sleep(0.25)
    for i in range(inicio,fim+1,passo):
        print(i,end=' ',flush=True)
        sleep(0.5)
    print('Fim!')


contagem(1,10,1)
contagem(10,0,-2)
print('Agora é sua vez de personalizar a contagem! ')
inicio = int(input('Iniício: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contagem(inicio,fim,passo)
