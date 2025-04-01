#!/usr/bin/env python3

n1 = int(input('Insira um valor: '))
resposta = 0
for i in range(n1,1,-1):
    if(n1 % i ==0 and i != n1):
        resposta = -1
        break        
    else:
        resposta = 1
if(resposta == 1):
    print('O número {} é primo!'.format(n1))
elif(resposta == -1):
    print('O número {} não é primo!'.format(n1))
