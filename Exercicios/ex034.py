#!/usr/bin/env python3

n1 = float(input('Digite o valor atual do salário: '))

if(n1>1250):
    print('Quem ganhava {} agora passa a ganhar R${}'.format(n1,n1*1.10)) #10%
else:
    print('Quem ganhava {} agora passa a ganhar R${}'.format(n1,n1*1.15)) #15%
