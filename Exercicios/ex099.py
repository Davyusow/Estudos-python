#!/usr/bin/env python3
from time import sleep
def maior(*num):
    print(f'{"-"*30}\nAnalisando os valores passados...')
    if len(num) > 0:
        Maior = num[0]
        for i in range(0,len(num)):
            if(num[i]>Maior):Maior = num[i]
            print(num[i],end=' ',flush=True); sleep(0.5)
        print(f'Foram informados {len(num)} números ao todo.')
        print(f'O maior valor informado foi {Maior}')
    else:
        print('Foram informados 0 ao todo.')
        print(f'O maior valor informado foi 0\n{"-"*30}')


maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()
