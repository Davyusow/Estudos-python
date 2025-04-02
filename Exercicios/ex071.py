#!/usr/bin/env python3

saqueSalvo = int(input('Digite o valor que deseja sacar: R$'))
saque = saqueSalvo
n50 = 0; n25 = 0; n10 = 0 ;n1 = 0
while(True):
    if(saque>=50):
        n50+=1
        saque-=50
    elif(saque>=25 and saque<50):
        n25+=1
        saque-=25
    elif(saque>=10 and saque <25):
        n10+=1
        saque-=10
    elif(saque>=1 and saque<10):
        n1+=1
        saque-=1
    if(saque==0): break

print('Serão necessárias: ')
if (n50>0): print(f'{n50} Notas de R$50') 
if (n25>0): print(f'{n25} Notas de R$25')
if (n10>0): print(f'{n10} Notas de R$10')
if (n1>0): print(f'{n1} Notas de R$1')